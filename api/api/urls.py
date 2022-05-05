from django.urls import path

from remessa.views import importar_remessa

urlpatterns = [
    path('importar-remessa', importar_remessa, name='importar_remessa'),
]
