from django.urls import path
from . views import listaproveedores, creaproveedor

urlpatterns = [
    path('', listaproveedores),
    path('nuevo/', creaproveedor),
]