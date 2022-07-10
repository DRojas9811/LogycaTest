from  django.db import models


class InventarioManager(models.Manager):
    def ListInventario(self):
        return self.filter()

class RegistroManager(models.Manager):
    def ListRegistro(self):
        return self.filter()
    def ListarRegistroByCliente(self,gln_cliente):
        return self.filter(inventarioFK__clienteFK__GLN__icontains=gln_cliente)
    def ListarRegistroBySucursal(self,gln_sucursal):
        return self.filter(inventarioFK__sucursalFK__GLN__icontains=gln_sucursal)
    def ListarRegistroByProducto(self,gln_producto):
        return self.filter(productoFK__GLN__icontains=gln_producto)
