from django import forms
from .models import CategoriaProducto, Producto, CategoriaPeso, Accesorios, Membresia, Inscripcion, Registro, Cliente, CrossFit, Venta
class VentaFrom(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Producto','Inscripcion', 'pagodiario']
        widgets = {
            'Producto': forms.TextInput(attrs={
                'placeholder': 'Ingrese producto',
                'class': 'form-group',
                'required': True
            }),
            'Inscripcion': forms.TextInput(attrs={
                'placeholder': 'Ingrese categoria',
                'class': 'form-group',
                'required': True
            }),
            'pagodiario': forms.TextInput(attrs={
                'placeholder': 'Ingrese precio',
                'class': 'form-group',
                'required': True
            }),
        }
class ClienteFrom(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula','nombre', 'apellido', 'telefono', 'estatura', 'peso', 'genero']
        widgets = {
            'cedula': forms.TextInput(attrs={
                'placeholder': 'Escriba su cedula',
                'class': 'form-group',
                'type': 'number',
                'required': True
            }),
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese su nombre',
                'class': 'form-group',
                'required': True
            }),
            'apellido': forms.TextInput(attrs={
                'placeholder': 'Ingrese su apellido',
                'class': 'form-group',
                'required': True
            }),
            'telefono': forms.TextInput(attrs={
                'placeholder': 'Escriba su telefono',
                'class': 'form-group',
                'type': 'number',
                'required': True
            }),
            'estatura': forms.TextInput(attrs={
                'placeholder': 'Ingrese su estatura',
                'class': 'form-group',
                'required': True
            }),
            'peso': forms.TextInput(attrs={
                'placeholder': 'Ingrese su peso',
                'class': 'form-group',
                'required': True
            }),
            'genero': forms.TextInput(attrs={
                'placeholder': 'Escriba su genero',
                'class': 'form-group',
                'type': 'number',
                'required': True
            }),
        }
class AccesorioFrom(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ['nombre', 'categoriaPeso']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre del producto',
                'class': 'form-group',
                'required': True
            }),
            'Categoria': forms.TextInput(attrs={
                'placeholder': 'Ingrese la categoria',
                'class': 'form-group',
                'required': True
            }),
        }
class MembresiaFrom(forms.ModelForm):
    class Meta:
        model = Membresia
        fields = ['membresia', 'pago']
        widgets = {
            'membresia': forms.TextInput(attrs={
                'placeholder': 'Escriba su cedula',
                'class': 'form-group',
                'type': 'number',
                'required': True
            }),
            'pago': forms.TextInput(attrs={
                'placeholder': 'Ingrese su nombre',
                'class': 'form-group',
                'required': True
            }),
        }