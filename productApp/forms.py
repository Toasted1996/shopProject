from django import forms
from .models import Categoria, Marca

class marcaForm(forms.ModelForm):
    class Meta:
        #Especificamos el modelo a usar
        model = Marca #Representa la clase en models.py
        #Especificamos los atributos del modelo a usar
        fields = '__all__' #Usamos todos los atributos del modelo
        #Configuraciones de los inputs
        widgets ={
            'nombre': forms.TextInput()
        }
        
        
class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets ={
            'nombre': forms.TextInput()
        }