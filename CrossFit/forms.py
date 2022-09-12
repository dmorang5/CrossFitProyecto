from django import forms
from .models import  Producto, Accesorios, Membresia, Cliente, Venta
class ProductoFrom(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'estado']

class VentaFrom(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Producto', 'cantidad', 'descripcion']

class ClienteFrom(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula','nombre', 'apellido', 'telefono', 'estatura', 'peso', 'genero']
        # widgets = {
        #     'cedula': forms.TextInput(attrs={
        #         'placeholder': 'Escriba su cedula',
        #         'class': 'form-group',
        #         'type': 'number',
        #         'required': True
        #     }),
        #     'nombre': forms.TextInput(attrs={
        #         'placeholder': 'Ingrese su nombre',
        #         'class': 'form-group',
        #         'required': True
        #     }),
        #     'apellido': forms.TextInput(attrs={
        #         'placeholder': 'Ingrese su apellido',
        #         'class': 'form-group',
        #         'required': True
        #     }),
        #     'telefono': forms.TextInput(attrs={
        #         'placeholder': 'Escriba su telefono',
        #         'class': 'form-group',
        #         'type': 'number',
        #         'required': True
        #     }),
        #     'estatura': forms.TextInput(attrs={
        #         'placeholder': 'Ingrese su estatura',
        #         'class': 'form-group',
        #         'required': True
        #     }),
        #     'peso': forms.TextInput(attrs={
        #         'placeholder': 'Ingrese su peso',
        #         'class': 'form-group',
        #         'required': True
        #     }),
        #     'genero': forms.Select(attrs={
        #         'placeholder': 'Escriba su genero',
        #         'class': 'form-group',
        #         'type': 'number',
        #         'required': True
        #     }),
        # }
class AccesorioFrom(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ['nombre', 'categoriaPeso', 'descripcion']
        # widgets = {
        #     'nombre': forms.TextInput(attrs={
        #         'placeholder': 'Ingrese el nombre del producto',
        #         'class': 'form-group',
        #         'required': True
        #     }),
        #     'Categoria': forms.TextInput(attrs={
        #         'placeholder': 'Ingrese la categoria',
        #         'class': 'form-group',
        #         'required': True
        #     }),
        #     'Descripcion': forms.TextInput(attrs={
        #         'placeholder': 'Ingrese la descripcion',
        #         'class': 'form-group',
        #         'required': True
        #     }),
        # }
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
