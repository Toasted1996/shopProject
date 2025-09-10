#Archivo creado para definir las URLs de la aplicacion de productos

from django.urls import path
from .views import marcas, categorias, productos, crearMarca, crearCategoria, crearProducto

urlpatterns = [
    path('marcas/', marcas, name = 'marcas'),
    path('crearMarca/', crearMarca, name='cmarca'), 
    path('categorias/', categorias, name = 'categorias'),
    path('crearCategoria/', crearCategoria, name='ccategoria'),
    path('productos/', productos, name = 'productos'),
    path('crearProducto/', crearProducto, name='cproducto')
]