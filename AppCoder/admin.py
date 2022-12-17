from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Local)
admin.site.register(Gerente)
admin.site.register(Empleado)
admin.site.register(Mercaderia)