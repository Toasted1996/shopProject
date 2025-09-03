#Archivo creado para definir las URLs de la aplicacion de productos

from django.urls import path
from .views import marcas

urlpatterns = [
    path('marcas/', marcas, name = 'marcas')
]