from django.urls import path
from .views import *

urlpatterns=[
    
    path('local1/', local1),
    path('Local/', Local, name='Local'),
    path('Gerente/', Gerente, name='Gerente'),
    path('Empleado/', Empleado, name='Empleado'),
    path('Mercaderia/', Mercaderia, name='Mercaderia'),
    path('', Inicio, name='Inicio'),

]
