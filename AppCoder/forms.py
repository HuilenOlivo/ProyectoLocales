from django import forms

class formulariolocal(forms.Form):
    nombre= forms.CharField(label="Nombre Curso", max_length=50)
    sucursal= forms.IntegerField(label="Comision")

class formulariogerente(forms.Form):
    nombre= forms.CharField(label="Nombre Gerente", max_length=50)
    apellido= forms.CharField(label="Apellido Gerente", max_length=50)
    email= forms.EmailField(label="Email Gerente")
    telefono= forms.IntegerField(label="Telefono Gerente")

class formularioempleado(forms.Form):
    nombre= forms.CharField(label="Nombre Empleado", max_length=50)
    apellido= forms.CharField(label="Apellido Empleado", max_length=50)
    email= forms.EmailField(label="Email Empleado")
    telefono= forms.IntegerField(label="Telefono empleado")


class formulariomercaderia(forms.Form):
    nombre= forms.CharField(label="Nombre Producto", max_length=50)
    marca= forms.CharField(label="Marca", max_length=50)
    fechaingreso= forms.DateField(label="Fecha de ingreso")
    cantidad= forms.IntegerField(label="cantidad")