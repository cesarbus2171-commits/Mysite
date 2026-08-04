from django.urls import path
from .views import listagrupos, creagrupos

urlpatterns = [
    path('', listagrupos),
    path('nuevo/', creagrupos),
]