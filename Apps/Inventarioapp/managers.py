from  django.db import models


class InventarioManager(models.Manager):
    def ListInventario(self):
        return self.filter().order_by("created_at")

class RegistroManager(models.Manager):
    def ListRegistro(self):
        return self.filter().order_by("created_at")
    def ListarRegistroByCliente(self,gln_cliente):
        return self.filter(inventarioFK__clienteFK__GLN__icontains=gln_cliente).order_by("created_at")
    def ListarRegistroBySucursal(self,gln_sucursal):
        return self.filter(inventarioFK__sucursalFK__GLN__icontains=gln_sucursal).order_by("created_at")
    def ListarRegistroByProducto(self,gln_producto):
        return self.filter(productoFK__GLN__icontains=gln_producto).order_by("created_at")
