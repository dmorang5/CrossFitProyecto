from django.db import models
producto_estado = [
    (1, "Disponible"),
    (2, 'No disponible')
]
genero = [
    (1, "Masculino"),
    (2, "Femenino")
]
inscripcion = [
    (1, "Mensual"),
    (2, "Semanal")
]
catePeso = [
    (1, "10kg"),
    (2, "20kg"),
    (3, "30kg")
]
accesorio = [
    (1, 'mancuerna'),
    (2, 'pesa'),
    (3, 'cuerda')
]

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    estado = models.IntegerField(
        null=False, blank=False,
        choices= producto_estado,
        default=1
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

#Accesorios

class Accesorios(models.Model):
    idAccesorio = models.AutoField(primary_key=True)
    nombre = models.IntegerField(
         null=False, blank=False,
         choices= accesorio,
         default=1)
    categoriaPeso = models.IntegerField(
         null=False, blank=False,
         choices= catePeso,
         default=1)
    descripcion = models.CharField(max_length=100, blank=False, null=True)

    class Meta:
        verbose_name = "Accesorio"
        verbose_name_plural = "Accesorios"

    def __str__(self):
        return self.descripcion
#Cliente
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    estatura = models.CharField(max_length=100, blank=True, null=True)
    peso = models.CharField(max_length=100, blank=True, null=True)
    genero = models.IntegerField(
        null=False, blank=False,
        choices= genero,
        default=1
    )
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.nombre

#Registro

#Inscripcion y membresia
class Membresia(models.Model):
    idMembresia = models.AutoField(primary_key=True)
    membresia = models.CharField(max_length=100, blank=True, null=True)
    pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Membresia"
        verbose_name_plural = "Membresias"


class Inscripcion(models.Model):
    idInscripcion = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaIns = models.DateTimeField(auto_now_add=True, auto_now=False)
    Membresia = models.IntegerField(
         null=False, blank=False,
         choices= inscripcion,
         default=1)

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"
    def __str__(self):
        return self.fechaIns, self.idCliente

#Venta
class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return self.descripcion

