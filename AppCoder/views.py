from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def local1 (request):
    Local1 = Local (nombre= 'Los Hermanos', sucursal=3)
    Local1.save()
    muestralocal1=f'Local Guradado: Nombre:{Local1.nombre}, Sucursal: {Local1.sucursal}'
    return HttpResponse(muestralocal1)

def Local (request):
    return render(request, 'AppCoder/local.html')

def Gerente (request):
    return render(request, 'AppCoder/gerente.html')

def Empleado (request):
    return render(request, 'AppCoder/empleado.html')

def Mercaderia (request):
    return render(request, 'AppCoder/mercaderia.html')

def Inicio (request):
    return render(request, 'AppCoder/inicio.html')

def FormularioLocal(request):
    if request.method=='POST':
        nombre=request.POST['nombre']
        sucursal=request.POST['sucursal']
        local=Local(nombre=nombre, sucursal=sucursal)
        local.save()
        return render (request, 'AppCoder/inicio.html', {'mensaje': 'Local registrado correstamente'})
    else:
        return render (request, 'AppCoder/formulariolocal.html')
