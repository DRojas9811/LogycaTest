from django.db import models
from .managers import ClienteManager, ProductoManager, SucursalManager


class CommonGLN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    GLN = models.BigIntegerField()

    class Meta:
        abstract = True


class Cliente(CommonGLN):
    objects = ClienteManager()

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return "Codigo Cliente: " + str(self.GLN)


class Sucursal(CommonGLN):
    objects = SucursalManager()

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return "Codigo Sucursal: " + str(self.GLN)


class Producto(CommonGLN):
    precio = models.DecimalField("valor", max_digits=10, decimal_places=2)
    objects = ProductoManager()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return "Codigo Producto: " + str(self.GLN)
