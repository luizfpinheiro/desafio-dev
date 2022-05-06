from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from remessa.models import Transacao, TipoTransacao
from .utils import CNAB


@require_http_methods(["POST"])
def importar_remessa(request):
    """ View utilizada para importacao do arquivo CNAB. Retorna os dados parseados."""

    if request.method == 'POST' and request.FILES['file']:
        upload = request.FILES['file']

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

                Transacao.objects.create(**transacao)

        return HttpResponse(remessa.transacoes)

@require_http_methods(["GET", "OPTIONS"])
def get_transacoes(request):
    """ View utilizada para listar transacoes guardadas na base de dados."""

    response = []
    if request.method == 'GET':

        queryset = Transacao.objects.all()
        for item in queryset:
            data = model_to_dict(item)
            data["valor"] = str(data["valor"])

            response.append(data)

        return JsonResponse(response, safe=False)