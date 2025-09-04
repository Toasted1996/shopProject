from django.shortcuts import render
from productApp.models import Marca, Categoria, Producto

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def marcas(request):
    # traemos todos los elementos de la lista de marcas
    lista = Marca.objects.all() #Marcas.objects.all() === select * from marcas
    data = { 'lista': lista,
            'titulo': 'Marcas'}
    return render(request, 'producto/marcas.html', data)

def categorias(request):
    lista = Categoria.objects.all()
    data = {
        'lista': lista,
        'titulo': 'Categorias'
    }
    return render (request, 'producto/categorias.html', data)

def productos(request):
    lista = Producto.objects.all()
    data = {
        'lista':lista,
        'titulo':'Productos'
    }
    return render(request, 'producto/productos.html', data)