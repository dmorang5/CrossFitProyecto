from django.shortcuts import render, redirect, HttpResponse
from urllib.request import Request
from CrossFit.forms import ClienteFrom, VentaFrom, AccesorioFrom, MembresiaFrom
from .models import Cliente, Venta, Accesorios, Membresia

def inicio(request):
    return render(request, "index.html")

def principal(request):
    return render(request, "pages/principal.html")

def venta(request):
    return render(request, "pages/ventas.html")

def nuevaVenta(request):
        return render(request,"pages/nuevaventa.html")
def crearVenta(request):
    if request.method == "POST":
        print("entro por post")
        venta_from = VentaFrom(request.POST)
        if venta_from.is_valid():
            venta_from.save()
        else:
            print("entro por get")
        venta_from = VentaFrom()
        ventas = Venta.objects.all()
    return render(request, "pages/nuevaventa.html", { 'VentaFrom': venta_from, 'ventas': ventas, 'accion': 'Guardar'})

def editarVenta(request):
    error, venta_from = None, None
    try:
        venta = Venta.objects.get(id=id)
        if request.method == "GET":
           venta_from = VentaFrom(instance=venta)
        else:
           venta_from = VentaFrom(request.POST,instance=venta)
           if venta_from.is_valid():
                venta_from.save()
                return redirect('venta')
    except Exception as e:
        error = e
        ventas = Venta.objects.all()
        return render(request, "pages/editventa.html", {'ventaForm': venta_from, 'venta': ventas, 'accion': 'Actualizar'})
def eliminarVenta(request,id):
    venta = Venta.objects.get(id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect("venta")
    return render(request,'pages/eliminarVenta.html',{'venta':venta})

def Accesorio(request):
    return render(request, "pages/equipos.html")

def nuevoAccesorio(request):
    return render(request, "pages/nuevoEquipo.html")

def crearAccesorio(request):
    if request.method == "POST":
        print("entro por post")
        accesorio_form = AccesorioFrom(request.POST)
        if accesorio_form.is_valid():
            accesorio_form.save()
        else:
            print("entro por get")
        accesorio_form = VentaFrom()
        accesorios = Accesorios.objects.all()
        return render(request, "pages/nuevoEquipo.html", {'AccesorioFrom': accesorio_form, 'accesorio': accesorios, 'accion': 'Guardar'})

def editarAccesorio(request):
    error, venta_form = None, None
    try:
        accesorio = Accesorios.objects.get(id=id)
        if request.method == "GET":
           accesorio_form = VentaFrom(instance=accesorio)
        else:
           accesorio_form = VentaFrom(request.POST,instance=accesorio)
           if accesorio_form.is_valid():
                accesorio_form.save()
                return redirect('accesorio')
    except Exception as e:
        error = e
        accesorios = Accesorios.objects.all()
        return render(request, "pages/equiposedit.html", {'accesorioFrom': accesorio_form, 'accesorio': accesorios, 'accion': 'Actualizar'})

def eliminarAccesorio(request,id):
    accesorio = Accesorios.objects.get(id=id)
    if request.method == 'POST':
        accesorio.delete()
        return redirect("accesorio")
    return render(request,'pages/eliminarEquipo.html',{'accesorio':accesorio})

def Cliente(request):
    return render(request, "pages/cliente.html")

def nuevoCliente(request):
    return render(request, "pages/nuevoCliente.html")

def crearCliente(request):
    if request.method == "POST":
        print("entro por post")
        cliente_form = ClienteFrom(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
        else:
            print("entro por get")
        cliente_form = VentaFrom()
        clientes = Cliente.objects.all()
        return render(request, "pages/nuevoCliente.html", {'ClienteFrom': cliente_form, 'cliente': clientes, 'accion': 'Guardar'})

def editarCliente(request):
    error, cliente_form = None, None
    try:
        cliente = Cliente.objects.get(id=id)
        if request.method == "GET":
           cliente_form = ClienteFrom(instance=cliente)
        else:
           cliente_form = ClienteFrom(request.POST,instance=cliente)
           if cliente_form.is_valid():
                cliente_form.save()
                return redirect('cliente')
    except Exception as e:
        error = e
        clientes = Cliente.objects.all()
        return render(request, "pages/editarcliente.html", {'ClienteFrom': cliente_form, 'cliente': clientes, 'accion': 'Actualizar'})

def eliminarCliente(request,id):
    cliente = Cliente().objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect("cliente")
    return render(request,'pages/eliminarCliente.html',{'cliente':cliente})