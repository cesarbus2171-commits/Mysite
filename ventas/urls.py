from django.urls import path
from . views import listaventas, creaventa

urlpatterns = [
    path('', listaventas),
    path('nuevo/', creaventa),
]