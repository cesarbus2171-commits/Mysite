from django.urls import path
from .views import creanominas, listanominas

urlpatterns = [
    path('', listanominas),
    path('nuevo/', creanominas),
]