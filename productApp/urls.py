#Archivo creado para definir las URLs de la aplicacion de productos

from django.urls import path
from .views import marcas, categorias, productos

urlpatterns = [
    path('marcas/', marcas, name = 'marcas'), 
    path('categorias/', categorias, name = 'categorias'),
    path('productos/', productos, name = 'productos')
]