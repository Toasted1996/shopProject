from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from productApp.forms import marcaForm, categoriaForm, productoForm, FiltroProd
from productApp.models import Marca, Categoria, Producto
from django.db.models import Q 

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

#Metodo para editar marca -- Redirecciona al form de marca
def editarMarca(request, id):
    #Obetenemos la marca por su id
    marca = Marca.objects.get(pk=id)
    #validamos si el metodo es post
    if request.method == 'POST':
            #se cargan los datos del form, instance para indicar que es edicion
        form = marcaForm(request.POST, instance = marca)
            #si el formulario es valido
        if form.is_valid():
            #guarda el formulario arroja mensaje exitoso
            form.save()
            messages.success(request, 'Marca editada correctamente')
            return redirect('marcas')  # Redirige después de guardar
    #Si no es post (GET)
    else:
        #recarga los datos del formulario
        form = marcaForm(instance=marca)
        
    #Datos para enviar al template (se ejecuta siempre)   
    data = {
        'titulo':'Editar marca',
        'form' : form,
        'ruta':'producto/marcas.html'
    }    
    return render(request, 'producto/create.html', data)


#Metodo para eliminar marca -- recibe el id de la marca
def eliminarMarca(request, id):
    marca = Marca.objects.get(pk=id)
    marca.delete()
    messages.success(request, 'Marca eliminada correctamente')
    return redirect(to='marcas')

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

#Metodo para editar categoria -- Redirecciona al form de categoria
def editarCategoria(request, id):
    cat = Categoria.objects.get(pk = id)
    if request.method == 'POST':
        form = categoriaForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria editada')
    else:
        form = categoriaForm(instance=cat)

    data = {
        'titulo':'Editar categoria',
        'form': form,
        'ruta':'producto/categorias.html'
    }
    return render(request, 'producto/create.html', data)

#Metodo para eliminar categoria -- recibe el id de la categoria
def eliminarCategoria(request, id):
    cat = Categoria.objects.get(pk=id)
    cat.delete()
    messages.success(request, 'Categoria eliminada')
    return redirect(to='producto/categorias.html')

#View para listar producto con filtro de busqueda !!REVISAR!!
def productos(request):
    lista = Producto.objects.all()
    form = FiltroProd(request.POST)
    texto = request.POST.get('filtro_texto')
    #Comprueba que texto no es nulo ni una cadena vacia
    if texto and texto != '':
        lista = lista.filter(Q(nombre__icontains=texto))
    data = {
        'lista':lista,
        'titulo':'Productos',
        'form': form
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
def verProducto(request, codigo):
    producto = Producto.objects.get(pk=codigo)
    data = {
        'descripcion': producto.descripcion,
        'titulo': producto.nombre     
    }
    return render (request, 'producto/detalle.html', data)

#Metodo para eliminar producto, recibe el codigo del producto 
def eliminarProducto(request, codigo):
    prod = get_object_or_404(Producto, pk=codigo)
    prod.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect(to='productos')

#Metodo para editar producto -- recibe el codigo del producto y lo redirecciona al form de producto
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