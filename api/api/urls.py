from django.urls import path

from remessa.views import importar_remessa, get_transacoes

urlpatterns = [
    path('importar-remessa', importar_remessa, name='importar_remessa'),
    path('transacoes', get_transacoes, name='get_transacoes'),
]
