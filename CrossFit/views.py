from django.shortcuts import render, redirect, HttpResponse
from urllib.request import Request
from CrossFit.forms import ClienteFrom, VentaFrom, AccesorioFrom, ProductoFrom
from .models import Cliente, Venta, Accesorios, Producto

class CrossFitView(HttpResponse):
    def inicio(request):
        return render(request, "index.html")

    def principal(request):
        return render(request, "pages/Principal.html")

    def venta(request):
        ventas = Venta.objects.all()
        return render(request, "pages/ventas.html", {"ventas": ventas})

    def nuevaVenta(request):
        data = {
            'formv': VentaFrom()
        }
        if request.method == 'POST':
            formulario = VentaFrom(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "mensaje enviado"
            else:
                data["formv"] = formulario
        return render(request, "pages/nuevaventa.html", data)

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
        return render(request, "pages/nuevaventa.html", {'VentaFrom': venta_from, 'ventas': ventas, 'accion': 'Guardar'})

    def editarVenta(request, id):
        venta = Venta.objects.filter(id=id).first()
        form = VentaFrom(instance=venta)
        return render(request, "pages/editventa.html", {"form":form, 'venta': venta})

    def actualizarVenta(request, id):
        venta = Venta.objects.get(id=id)
        form = VentaFrom(request.POST, instance=venta)
        if form. is_valid():
            form.save()
        ventas = Venta.objects.all()
        return render(request, "pages/ventas.html", {"ventas":ventas})

    def eliminarVenta(request,id):
        venta = Venta.objects.get(id=id)
        if request.method == 'POST':
            venta.delete()
            return redirect("venta")
        return render(request,'pages/eliminarVenta.html',{'venta':venta})

    def Accesorio(request):
        accesorio = AccesorioFrom()
        return render(request, "pages/equipos.html",{"accesorio": accesorio})

    def AccesorioR(request):
        accesorio = AccesorioFrom()
        return render(request, "pages/nuevoequipo.html", {"accesorio": accesorio})

    def procesarAccesorio(request):
        accesorio = AccesorioFrom()
        if accesorio.is_valid():
            accesorio.save()
            accesorio = AccesorioFrom()
        return render(request, "pages/equipos.html", {"accesorio": accesorio, "mensaje": 'OK'})
    # def nuevoAccesorio(request):
    #     data = {
    #         'form': AccesorioFrom()
    #     }
    #     if request.method == 'POST':
    #         formulario = AccesorioFrom(data=request.POST)
    #         if formulario.is_valid():
    #             formulario.save()
    #             data["mensaje"] = "mensaje enviado"
    #         else:
    #             data["form"] = formulario
    #     return render(request, "pages/nuevoequipo.html", data)
    #
    # def crearAccesorio(request):
    #     if request.method == "POST":
    #         print("entro por post")
    #         accesorio_form = AccesorioFrom(request.POST)
    #         if accesorio_form.is_valid():
    #             accesorio_form.save()
    #         else:
    #             print("entro por get")
    #         accesorio_form = VentaFrom()
    #         accesorios = Accesorios.objects.all()
    #         return render(request, "pages/nuevoequipo.html", {'AccesorioFrom': accesorio_form, 'accesorio': accesorios, 'accion': 'Guardar'})
    #
    # def editarAccesorio(request):
    #     error, venta_form = None, None
    #     try:
    #         accesorio = Accesorios.objects.get(id=id)
    #         if request.method == "GET":
    #            accesorio_form = VentaFrom(instance=accesorio)
    #         else:
    #            accesorio_form = VentaFrom(request.POST,instance=accesorio)
    #            if accesorio_form.is_valid():
    #                 accesorio_form.save()
    #                 return redirect('accesorio')
    #     except Exception as e:
    #         error = e
    #         accesorios = Accesorios.objects.all()
    #         return render(request, "pages/equiposedit.html", {'accesorioFrom': accesorio_form, 'accesorio': accesorios, 'accion': 'Actualizar'})
    #
    # def eliminarAccesorio(request,id):
    #     accesorio = Accesorios.objects.get(id=id)
    #     if request.method == 'POST':
    #         accesorio.delete()
    #         return redirect("accesorio")
    #     return render(request,'pages/eliminarEquipo.html',{'accesorio':accesorio})

    def Cliente(request):
        cliente = Cliente.objects.all()
        return render(request, "pages/cliente.html" , {"clientes": cliente})

    def nuevoCliente(request):
        data = {
            'form': ClienteFrom()
        }
        if request.method == 'POST':
            formulario = ClienteFrom(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "mensaje enviado"
            else:
                data["form"] = formulario
        return render(request, "pages/nuevocliente.html", data)

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
            return render(request, "pages/nuevocliente.html", {'ClienteFrom': cliente_form, 'cliente': clientes, 'accion': 'Guardar'})

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
        cliente = Cliente.objects.get(id=id)
        if request.method == 'POST':
            cliente.delete()
            return redirect("cliente")
        return render(request,'pages/eliminarCliente.html',{'cliente':cliente})

    def ProductoForm(request):
        productos = Producto.objects.all()
        return render(request, "pages/producto.html",{"productos": productos})

    def nuevoProducto(request):
        data = {
            'form': ProductoFrom()
        }
        if request.method == 'POST':
            formulario = ProductoFrom(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"]="mensaje enviado"
            else:
                data["form"]=formulario
        return render(request, "pages/nuevoProducto.html", data)

    def crearProducto(request):
        # if request.method == "POST":
        #     print("entro por post")
        #     producto_form = ProductoFrom(request.POST)
        #     if producto_form.is_valid():
        #         producto_form.save()
        #     else:
        #         print("entro por get")
        #     producto_form = VentaFrom()
        #     productos = Producto.objects.all()
        return render(request, "pages/producto.html")
    def editarProducto(request, id):
        producto = Producto.objects.filter(id=id).first()
        form = ProductoFrom(instance=producto)
        return render(request, "pages/editarProducto.html", {"form":form, 'producto': producto})

    def actualizarProducto(request, id):
        producto = Producto.objects.get(id=id)
        form = ProductoFrom(request.POST, instance=producto)
        if form. is_valid():
            form.save()
        productos = Producto.objects.all()
        return render(request, "pages/producto.html", {"productos":productos})

    def eliminarProducto(request,id):
        producto = Producto.objects.get(id=id)
        if request.method == 'POST':
            producto.delete()
            return redirect("producto")
        return render(request,'pages/eliminarProducto.html',{'producto':producto})