from django.db import models

# Create your models here.
class Marca(models.Model):
    #Atributos de la clase, Charfield es el tipo de dato del atributo, 
    #max_length es la cantidad de letras que podemos asignar al atributo
    nombre = models.CharField(max_length=30)
    #Metodo str y sirve para mostrar el objeto
    def __str__(self):
        return self.nombre
    #Meta sirve para definir algunas variables
    class Meta:
        #db_table es nombre de la tabla en la base de datos
        db_table = 'marca'
        
class Categoria(models.Model):
    #Atributos de la clase, CharField es el tipo de datos del atributo
    nombre =  models.CharField(max_length=30)
    #Metodo str y sirve para mostar el objeto
    def __str__(self):
        return self.nombre
    #Meta para definir algunas variables    
    class Meta:
        db_table = 'categoria'
        
class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True),
    nombre = models.CharField(max_length=100),
    precio = models.IntegerField(),
    
    #PositiveBigIntegerField permite solo valores positivos
    stock = models.PositiveBigIntegerField(),
    
    #TextField permite texto mas extenso, null=True dignifica que este campo puede ser nulo 
    descripcion = models.TextField(null=True),
    foto = models.ImageField(upload_to='productos'),
    marca = models.ForeignKey(Marca, on_delete = models.RESTRICT)
    
    #on_delete = models.CASCADE si eleimina la categoria, se elimina todos los productos, sin embargo lo ideal seria que sera RESTRICT para que no pueda eliminar todo
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'productos'