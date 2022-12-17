from django.urls import path
from .views import *

urlpatterns=[
    
    path('local1/', local1),
    path('Locales/', Local, name='Local'),
    path('Gerentes/', Gerente, name='Gerente'),
    path('Empleados/', Empleado, name='Empleado'),
    path('Mercaderia/', Mercaderia, name='Mercaderia'),
    path('', Inicio, name='Inicio'),
    path('formulariolocal/', FormularioLocal, name='formulariolocal')

]
