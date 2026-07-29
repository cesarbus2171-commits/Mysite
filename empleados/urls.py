from django.urls import path
from .views import listaempleados, creaempleado

urlpatterns = [
    path('', listaempleados),
    path('nuevo/', creaempleado),
]