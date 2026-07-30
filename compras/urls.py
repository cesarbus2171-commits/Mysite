from django.urls import path
from .views import listacompras, creacompras

urlpatterns = [
    path('', listacompras,),
    path('nuevo/', creacompras),
]