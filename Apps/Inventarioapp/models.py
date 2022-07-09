from django.db import models
from ..Informacionapp.models import (
    Cliente,
    Sucursal,
    Producto,
)
from .managers import InventarioManager, RegistroManager
# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Inventario(TimeStampedModel):
    clienteFK = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursalFK = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    objects = InventarioManager()

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

    def __str__(self):
        return "Cliente: " + str(self.clienteFK) + " - Sucursal: "+str(self.sucursalFK)


class Registro(TimeStampedModel):
    inventarioFK = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    productoFK = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    objects = RegistroManager()

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return "Producto: " + str(self.productoFK) + " del inventario: " + str(self.inventarioFK)
