from django.shortcuts import render
from productApp.models import Marca

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def marcas(request):
    # traemos todos los elementos de la lista de marcas
    lista = Marca.objects.all() #Marcas.objects.all() === select * from marcas
    data = { 'lista': lista,
            'titulo': 'Marcas'}
    return render(request, 'producto/marcas.html', data)