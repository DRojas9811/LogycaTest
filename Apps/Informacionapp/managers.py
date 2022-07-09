from  django.db import models


class ClienteManager(models.Manager):
    def ListCliente(self):
        return self.filter()


class SucursalManager(models.Manager):
    def ListSucursal(self):
        return self.filter()

class ProductoManager(models.Manager):
    def ListProducto(self):
        return self.filter()


