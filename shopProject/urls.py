"""
URL configuration for shopProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from productApp.views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = 'inicio'),
    
    #Importamos el archivo URLs de la aplicacion de productos
    path('producto/', include('productApp.urls'))
]

# Configuración para archivos estáticos (CSS, JS, imágenes del proyecto)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Configuración para archivos media (imágenes subidas por usuarios)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
