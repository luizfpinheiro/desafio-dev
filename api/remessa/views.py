from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .utils import CNAB


@require_http_methods(["POST"])
def importar_remessa(request):
    if request.method == 'POST' and request.FILES['file']:
        upload = request.FILES['file']

        remessa = CNAB(arquivo=upload)

        return HttpResponse(remessa.transacoes)
