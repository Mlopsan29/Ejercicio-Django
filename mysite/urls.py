"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from blog import views # Importamos las vistas del blog
from gimnasio import views as gimnasio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('animales/', views.lista_animales, name='lista_animales'),
    path('protectoras/', views.lista_protectoras, name='lista_protectoras'),
    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),
    path('socios/', gimnasio_views.lista_socios, name='lista_socios'),
    path('entrenadores/', gimnasio_views.lista_entrenadores, name='lista_entrenadores'),
    path('clases/', gimnasio_views.lista_clases, name='lista_clases'),
]