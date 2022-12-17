from django.urls import path
from .views import *


urlpatterns=[
    
    path('local1/', local1),
    path('Local/', Local),
    path('Gerente/', Gerente),
    path('Empleado/', Empleado),
    path('Mercaderia/', Mercaderia),
    path('', Inicio),


]

