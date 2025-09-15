from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from productApp.forms import marcaForm, categoriaForm, productoForm
from productApp.models import Marca, Categoria, Producto

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

#View para listar marcas
def marcas(request):
    # traemos todos los elementos de la lista de marcas
    lista = Marca.objects.all() #Marcas.objects.all() === select * from marcas
    data = { 'lista': lista,
            'titulo': 'Marcas'}
    return render(request, 'producto/marcas.html', data)

#Metodo para crear Marca -- FORMULARIO
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

#View para listar categoria
def categorias(request):
    lista = Categoria.objects.all()
    data = {
        'lista': lista,
        'titulo': 'Categorias'
    }
    return render (request, 'producto/categorias.html', data)

#Metodo para crear categoria -- FORMULARIO
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

#View para listar producto 

def productos(request):
    lista = Producto.objects.all()
    data = {
        'lista':lista,
        'titulo':'Productos'
    }
    return render(request, 'producto/productos.html', data)

#Metodo para crear Producto -- FORMULARIO
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

#View para ver detalle producto
def verProducto(request, id):
    producto = Producto.objects.get(pk=id)
    data = {
        'descripcion': producto.descripcion,
        'titulo': producto.nombre     
    }
    return render (request, 'producto/detalle.html', data)


def eliminarProducto(request, codigo):
    #Buscamos el producto por su codigo:
    prod = Producto.objects.get(pk=codigo)
    #preguntamos si el producto tiene foto asociada
    if prod.foto:
        #eliminamos la foto del producto
        prod.foto.delete()
    #eliminamos el producto
    prod.delete()
    #permite redireccionar al template de productos
    return redirect(to="/producto/productos.html")
    
    
def editarProducto(request, codigo):
    prod = Producto.objects.get(pk=codigo)
    if request.method == 'POST':
        if request.FILES.get('foto', False):
            if prod.foto:
                prod.foto.delete()
                form = productoForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado correctamente')
    else:
        form = productoForm(instance=prod)

    data = {
        'titulo':'Editar producto',
        'form': form,
        'ruta':'producto/productos.html'
    }
    return render(request, 'producto/create.html', data)  