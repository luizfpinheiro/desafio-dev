from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from remessa.models import Transacao, TipoTransacao
from .utils import CNAB


@require_http_methods(["POST"])
def importar_remessa(request):
    """ View utilizada para importacao do arquivo CNAB. Retorna os dados parseados."""

    if request.method == 'POST' and request.FILES.get('file', None):
        upload = request.FILES.get('file', None)

        remessa = CNAB(arquivo=upload)
        if remessa:
            for transacao in remessa.transacoes:
                data = transacao['dt_cadastro']
                hora = transacao.pop('hora')

                dt_cadastro = datetime(
                    int(data[:4]), int(data[4:6]), int(
                        data[6:8]),  # YYYY-MM-DD
                    int(hora[:2]), int(hora[2:4]), int(hora[4:6])  # H-M-S
                )
                transacao['dt_cadastro'] = dt_cadastro

                tipo_transacao = TipoTransacao.objects.get(
                    id=transacao["tipo"])
                transacao["tipo"] = tipo_transacao

                if not tipo_transacao.bo_entrada:
                    transacao["valor"] = -transacao["valor"]

                Transacao.objects.create(**transacao)

            return HttpResponse(remessa.transacoes)
    else:
        return JsonResponse({ "message": "Necessário upload do arquivo." }, status=400)


@require_http_methods(["GET", "OPTIONS"])
def get_transacoes(request):
    """ View utilizada para listar transacoes guardadas na base de dados."""

    response = []

    if request.method == 'GET':

        saldo_por_loja = Transacao.objects.values(
            'nome_loja').annotate(Sum('valor'))

        for item in saldo_por_loja:
            nome_loja = item["nome_loja"]

            transacoes = Transacao.objects.filter(nome_loja=nome_loja).values(
                'id', 'tipo__descricao', 'valor', 'cpf', 'cartao', 'nome_representante', 'nome_loja'
            )

            response.append({
                "nome_loja": nome_loja,
                "saldo": "{:.2f}".format(item["valor__sum"]),
                "transacoes": [t for t in transacoes]
            })

        return JsonResponse(response, safe=False)
