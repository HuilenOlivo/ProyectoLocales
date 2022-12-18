from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *

from django.urls import reverse_lazy

from django.views.generic import *


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
    if request.method=="POST":
        form= formulariolocal(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre= informacion["nombre"]
            sucursal= informacion["sucursal"]
            local= Local(nombre=nombre, sucursal=sucursal)
            local.save()
            return render(request, "AppCoder/inicio.html" ,{"mensaje": "Curso guardado correctamente"})
        else:
            return render(request, "AppCoder/formulariolocal.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:

        formulario= formulariolocal()
        return render (request, "AppCoder/formulariolocal.html", {"form": formulario})

def FormularioGerente(request):
    if request.method=="POST":
        form= formulariogerente(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            telefono= telefono ["telefono"]
            formulariogerente1= Gerente(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            formulariogerente1.save()
           
            return render(request, "AppCoder/gerente.html" ,{"Gerente":formulariogerente1, "mensaje": "Gerente guardado correctamente"})
        else:
            return render(request, "AppCoder/formulariogerente.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulariogerente1= formulariogerente()
        return render (request, "AppCoder/ProfeFormulario.html", {"form": formulariogerente})


def FormularioEmpleado(request):
    if request.method=="POST":
        form= formularioempleado(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            telefono= telefono ["telefono"]
            formularioempleado1= Empleado(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            formularioempleado1.save()
           
            return render(request, "AppCoder/empleado.html" ,{"Empleado":formularioempleado1, "mensaje": "Empleado guardado correctamente"})
        else:
            return render(request, "AppCoder/formularioempleado.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formularioempleado1= formulariogerente()
        return render (request, "AppCoder/formularioempleado.html", {"form": formularioempleado})


def FormularioMercaderia(request):
    if request.method=="POST":
        form= formulariomercaderia(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            marca= informacion["marca"]
            fechaingreso= informacion["fechaingreso"]
            cantidad= informacion ["cantidad"]
            formulariomercaderia1= Mercaderia(nombre=nombre, marca=marca, fechaingreso=fechaingreso, cantidad=cantidad)
            formulariomercaderia1.save()
            mercaderia=Mercaderia.objects.all()
            return render(request, "AppCoder/mercaderia.html" ,{"Empleado":mercaderia, "mensaje": "Informacion de Mercadería guardado correctamente"})
        else:
            return render(request, "AppCoder/formulariomercaderia.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulariomercaderia1= formulariogerente()
        return render (request, "AppCoder/formulariomercaderia.html", {"form": formulariomercaderia})

def buscarsucursal(request):
    return render (request, "AppCoder/buscarlocal.html")
    
def buscar (request):

    sucursal=request.GET['sucursal']
    if sucursal!="":
        local=Local.objects.filter (sucursal=sucursal)

        return render(request, "AppCoder/resultadosdebusqueda.html", {'local': local})
    else:
        return render (request, 'AppCoder/buscarsucurcal.html', {'mensaje': 'ingrese una sucuarsal para buscar'})