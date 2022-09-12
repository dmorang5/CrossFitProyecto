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
from CrossFit.views import CrossFitView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CrossFitView.inicio,name="inicio" ),
    path('principal/', CrossFitView.principal, name="principal"),
    #Venta
    path('venta/', CrossFitView.venta, name="venta"),
    path('nuevaVenta/',CrossFitView.nuevaVenta,name="nuevaVenta" ),
    path('editarVenta/<int:id>', CrossFitView.editarVenta, name="editarVenta"),
    path('actualizarVenta<int:id>', CrossFitView.actualizarVenta, name="actualizarVenta"),
    path('crearVenta/', CrossFitView.crearVenta, name="crearVenta"),
    path('eliminarVenta/', CrossFitView.eliminarVenta, name="eliminarVenta"),
    #Accesorio
    path('accesorio/',CrossFitView.Accesorio,name="accesorio" ),
    path ('registrarAccesorio/', CrossFitView.AccesorioR, name="registrarAccesorio"),
    path ('guardarAccesorio/', CrossFitView.procesarAccesorio, name="guardarAccesorio"),
    #Cliente
    path('cliente/',CrossFitView.Cliente,name="cliente" ),
    path('nuevoCliente/', CrossFitView.nuevoCliente, name="nuevoCliente"),
    path('editarCliente/<int:id>', CrossFitView.editarCliente, name="editarCliente"),
    path('crearCliente/', CrossFitView.crearCliente, name="crearCliente"),
    path('eliminarCliente/<int:id>', CrossFitView.eliminarCliente, name="eliminarCliente"),
    #Producto
    path('CrearProducto/',CrossFitView.ProductoForm,name="producto" ),
    path ('FormProducto/',CrossFitView.crearProducto, name="FormProducto"),
    path('nuevoProducto/', CrossFitView.nuevoProducto, name="nuevoProducto"),
    path('editarProducto/<int:id>', CrossFitView.editarProducto, name="editarProducto"),
    path('eliminarProducto/<int:id>', CrossFitView.eliminarProducto, name="eliminarProducto"),
]
