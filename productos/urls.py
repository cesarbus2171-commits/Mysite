from django.urls import include, path
from .views import listaproductos, creaproductos

urlpatterns = [
    path('', listaproductos),
    path('nuevo/', creaproductos),
]