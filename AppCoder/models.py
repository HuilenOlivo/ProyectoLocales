from django.db import models

# Create your models here.

class Local (models.Model):
    nombre= models.CharField(max_length=80)
    sucursal= models.IntegerField()

class Gerente (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    telefono= models.IntegerField()

class Empleado (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    telefono= models.IntegerField()

class Mercaderia (models.Model):
    nombre= models.CharField(max_length=50)
    marca= models.CharField(max_length=50)
    fechaingreso=models.DateField()
    cantidad= models.IntegerField()



