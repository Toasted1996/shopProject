#Archivo creado para definir las URLs de la aplicacion de productos

from django.urls import path
from .views import marcas, categorias, productos, crearMarca, crearCategoria, crearProducto, eliminarProducto, verProducto, editarProducto, editarCategoria, eliminarCategoria, editarMarca, eliminarMarca

urlpatterns = [
    # CRUD MARCA
    path('marcas/', marcas, name = 'marcas'),
    path('crearMarca/', crearMarca, name='cmarca'),
    path('editarMarca/<int:id>/editar', editarMarca, name='editarMarca'),
    path('eliminarMarca/<int:id>/eliminar', eliminarMarca, name='eliminarMarca'),
    # CRUD CATEGORIA 
    path('categorias/', categorias, name = 'categorias'),
    path('crearCategoria/'  , crearCategoria, name='ccategoria'),
    path('editarCategoria/<int:id>/editar', editarCategoria, name='editarCategoria'),
    path('eliminarCategoria/<int:id>/eliminar', eliminarCategoria, name='eliminarCategoria'),
    # CRUD PRODUCTO
    path('productos/', productos, name = 'productos'),
    path('crearProducto/', crearProducto, name='cproducto'),
    path('producto/<int:codigo>/', verProducto, name= 'verProducto'),
    path('producto/<int:codigo>/eliminar/', eliminarProducto, name= 'eliminarProducto'),
    path('producto/<int:codigo>/editar', editarProducto, name= 'editarProducto')
]