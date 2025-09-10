from django.contrib import messages
from django.shortcuts import render
from productApp.forms import marcaForm, categoriaForm, productoForm
from productApp.models import Marca, Categoria, Producto

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

#VISTA PARA LISTAR MARCAS
def marcas(request):
    # traemos todos los elementos de la lista de marcas
    lista = Marca.objects.all() #Marcas.objects.all() === select * from marcas
    data = { 'lista': lista,
            'titulo': 'Marcas'}
    return render(request, 'producto/marcas.html', data)

#METODO PARA CREAR MARCA -- FORMULARIO
def crearMarca(request):
    form = marcaForm()
    data={
        'titulo': 'Crear Marca',
        'form': form,
        'ruta': '/marcas/'
    }
    
    if request.method == 'POST':
        # cargar los datos del formulario
        form = marcaForm(request.POST)
        # si el formulario es valido
        if form.is_valid():
        # guardar el formulario en la base de datos
            form.save()
            # enviamos mensaje de éxito
        messages.success(request,'Marca creada correctamente')
    return render(request, 'producto/create.html', data)

#VISTA PARA LISTAR CATEGORIA
def categorias(request):
    lista = Categoria.objects.all()
    data = {
        'lista': lista,
        'titulo': 'Categorias'
    }
    return render (request, 'producto/categorias.html', data)

#METODO PARA CREAR CATEGORIA -- FORMULARIO
def crearCategoria(request):
    form = categoriaForm()
    data= {
        'titulo': 'Crear Categoria',
        'form': form,
        'ruta': 'producto/categorias.html'
    }
    
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Categoria creada correctamente')
    return render(request, 'producto/create.html', data)

#VISTA PARA LISTAR PRODUCTOS
def productos(request):
    lista = Producto.objects.all()
    data = {
        'lista':lista,
        'titulo':'Productos'
    }
    return render(request, 'producto/productos.html', data)

#METODO PARA CREAR PRODUCTO -- FORMULARIO
def crearProducto(request):
    if request.method == 'POST':
        form = productoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente')
    else:
        form = productoForm()
    
    data = {
        'titulo':'Crear producto',
        'form': form,
        'ruta':'producto/productos.html'
    }
    return render(request, 'producto/create.html', data)