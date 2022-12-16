from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def local1 (request):
    Local1 = Local (nombre= 'Los Hermanos', sucursal=3)
    Local1.save()
    muestralocal1=f'Local Guradado: Nombre:{Local1.nombre}, Sucursal: {Local1.sucursal}'
    return HttpResponse(muestralocal1)