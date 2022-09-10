from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    idCategoriaProducto = models.AutoField(primary_key=True)
    categoriaProducto = models.CharField(max_length=100, blank=False, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoriaProducto

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    categoriaProducto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

#Accesorios
class CategoriaPeso(models.Model):
    idCategoriaPeso = models.AutoField(primary_key=True)
    categoriaPeso = models.CharField(max_length=100, blank=False, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.descripcion

class Accesorios(models.Model):
    idAccesorio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    categoriaPeso = models.ForeignKey(CategoriaPeso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Accesorio"
        verbose_name_plural = "Accesorios"

    def __str__(self):
        return self.nombre

#Cliente
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    estatura = models.CharField(max_length=100, blank=True, null=True)
    peso = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.nombre, self.apellido, self.cedula

#Registro
class Registro(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    horaIng = models.TimeField(auto_now_add=False, auto_now=True)
    horaSalida = models.TimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
    def __str__(self):
        return self.idCliente

#Inscripcion y membresia
class Membresia(models.Model):
    idMembresia = models.AutoField(primary_key=True)
    membresia = models.CharField(max_length=100, blank=True, null=True)
    pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Membresia"
        verbose_name_plural = "Membresias"
    def __str__(self):
        return self.membresia

class Inscripcion(models.Model):
    idInscripcion = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaIns = models.DateTimeField(auto_now_add=True, auto_now=False)
    idMembresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"
    def __str__(self):
        return self.fechaIns, self.idCliente

#Venta
class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)

    pagodiario = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
    def __str__(self):
        return self.Producto, self.Inscripcion, self.pagodiario

#Crossfit
class CrossFit(models.Model):
    idCrossFit = models.AutoField(primary_key=True)
    idAccesorios = models.ForeignKey(Accesorios, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idInscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CrossFit"
        verbose_name_plural = "CrossFit"
    def __str__(self):
        return self.idAccesorios, self.idProducto, self.idInscripcion
