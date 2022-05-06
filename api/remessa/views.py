from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from remessa.models import Transacao, TipoTransacao
from .utils import CNAB


@require_http_methods(["POST"])
def importar_remessa(request):
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
