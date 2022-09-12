"""CrossFitProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from CrossFit.views import inicio, principal, crearVenta, editarVenta, eliminarVenta, crearAccesorio, editarAccesorio, \
    eliminarAccesorio, crearCliente, editarCliente, eliminarCliente, nuevoCliente, nuevaVenta, nuevoAccesorio, venta, \
    Accesorio, Cliente, eliminarProducto, editarProducto, nuevoProducto, ProductoForm, crearProducto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio" ),
    path('principal/', principal, name="principal"),
    #Venta
    path('venta/', venta, name="venta"),
    path('nuevaVenta/',nuevaVenta,name="nuevaVenta" ),
    path('editarVenta/<int:id>', editarVenta, name="editarVenta"),
    path('crearVenta/', crearVenta, name="crearVenta"),
    path('eliminarVenta/<int:id>', eliminarVenta, name="eliminarVenta"),
    #Accesorio
    path('accesorio/',Accesorio,name="accesorio" ),
    path('nuevoAccesorio/', nuevoAccesorio, name="nuevoAccesorio"),
    path('crearAccesorio/', crearAccesorio, name="crearAccesorio"),
    path('editarAccesorio/<int:id>', editarAccesorio, name="editarAccesorio"),
    path('eliminarAccesorio/<int:id>', eliminarAccesorio, name="eliminarAccesorio"),
    #Cliente
    path('cliente/',Cliente,name="cliente" ),
    path('nuevoCliente/', nuevoCliente, name="nuevoCliente"),
    path('editarCliente/<int:id>', editarCliente, name="editarCliente"),
    path('crearCliente/', crearCliente, name="crearCliente"),
    path('eliminarCliente/<int:id>', eliminarCliente, name="eliminarCliente"),
    #Producto
    path('CrearProducto/',ProductoForm,name="producto" ),
    path ('FormProducto/',crearProducto, name="FormProducto"),
    path('nuevoProducto/', nuevoProducto, name="nuevoProducto"),
    path('editarProducto/<int:id>', editarProducto, name="editarProducto"),
    path('eliminarProducto/<int:id>', eliminarProducto, name="eliminarProducto"),
]
