from  django.db import models


class InventarioManager(models.Manager):
    def ListInventario(self):
        return self.filter()

class RegistroManager(models.Manager):
    def ListRegistro(self):
        return self.filter()
