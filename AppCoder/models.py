from django.db import models

# Create your models here.

class Local (models.Model):
    usuario= models.CharField(max_length=80)
    sucursal= models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.sucursal}'


class Gerente (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    telefono= models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'


class Empleado (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    telefono= models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

class Mercaderia (models.Model):
    nombre= models.CharField(max_length=50)
    marca= models.CharField(max_length=50)
    fechaingreso=models.DateField()
    cantidad= models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.marca}'



