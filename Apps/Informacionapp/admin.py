from django.contrib import admin

from .models import Cliente,Sucursal,Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Sucursal)
admin.site.register(Producto)