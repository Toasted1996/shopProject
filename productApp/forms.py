from django import forms
from .models import Categoria, Marca, Producto

#Modelo de datos para el formulario de marca
class marcaForm(forms.ModelForm):
    class Meta:
        #Especificamos el modelo a usar
        model = Marca #Representa la clase en models.py
        #Especificamos los atributos del modelo a usar
        fields = '__all__' #Usamos todos los atributos del modelo
        #Configuraciones de los inputs -- Estilos y demas
        widgets ={
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre de la marca'
            })
        }

#Modelo de datos para el formulario de categoria        
class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets ={
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre de la categoria'
            })
        }

#Modelo de datos para el formulario de producto
class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets ={
            'nombre': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Descripcion',
                'rows': 3,
                'style': 'resize:none;'
            }),
            'precio': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Precio producto',
                'step': '1',
                'min': '0'
                
            }),
            'stock': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Stock producto',
                'step': '1',
                'min': '0'
            }),
            'categoria': forms.Select(attrs={
                'class':'form-select',
                'placeholder':'Selecciona una categoria'
            }),
            'marca': forms.Select(attrs={
                'class':'form-select',
                'placeholder':'Selecciona una marca'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class':'form-control',
                'placeholder':'Sube una imagen'
            })
        }

#Modelo de datos para el formulario de filtro producto
class FiltroProd(forms.Form):
    #Filtro para buscar texto en los productos
    texto = forms.CharField(required=False)
    #filtro para buscar por marca, queryset trae el listado de marcas
    #emptylabel es para que no haya ninguna marca seleccionada por defecto
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label='Seleccione una marca', required=False)