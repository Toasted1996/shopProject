# crear proyecto 
django-admin startproject shopProject
# acceder a carpeta del proyecto
cd shopProject
# crear app
django-admin startapp productoApp
# crear carpetas static y templates
mkdir static
mkdir templates
# recuerda agregar la app a settings y las carpetas creadas
# ejecutar servidor
py manage.py runserver

# Instalar librerías desde requirments.txt
pip install -r requirements.txt

# Crear la migracion
py manage.py makemigrations

# Ejecutar la migracion
py manage.py migrate