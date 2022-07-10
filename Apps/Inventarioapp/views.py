from .serializers import (AllRegistroSerializer, InventarioPagination,
                          InventarioSerializer,
                          RegistroSerializer,
                          AllRegistroSerializer,
                          )
from .models import Inventario, Registro
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from Apps.Inventarioapp import models
# Create your views here.


class ListInventarioView(ListAPIView):
    serializer_class = InventarioSerializer
    pagination_class = InventarioPagination

    def get_queryset(self):
        return Inventario.objects.ListInventario()


class ListRegistroView(ListAPIView):
    serializer_class = RegistroSerializer
    pagination_class = InventarioPagination
    def get_queryset(self):
        return Registro.objects.ListRegistro()


class ListAllRegistroView(ListAPIView):
    serializer_class = AllRegistroSerializer
    pagination_class = InventarioPagination

    def get_queryset(self):
        return Registro.objects.ListRegistro()

class ListRegistrobyClienteView(ListAPIView):
    serializer_class = AllRegistroSerializer
    pagination_class = InventarioPagination

    def get_queryset(self):
        gln_cliente=self.kwargs["GLN_cliente"]
        return Registro.objects.ListarRegistroByCliente(gln_cliente)

class ListRegistrobySucursalView(ListAPIView):
    serializer_class = AllRegistroSerializer
    pagination_class = InventarioPagination

    def get_queryset(self):
        gln_Sucursal=self.kwargs["GLN_Sucursal"]
        return Registro.objects.ListarRegistroBySucursal(gln_Sucursal)
class ListRegistrobyProductoView(ListAPIView):
    serializer_class = AllRegistroSerializer
    pagination_class = InventarioPagination

    def get_queryset(self):
        gln_Producto=self.kwargs["GLN_Producto"]
        return Registro.objects.ListarRegistroByProducto(gln_Producto)


class CreateRegistroView(CreateAPIView):
    serializer_class = AllRegistroSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # capturar los valores de data, crear instancias y agegar al modelo
        new_Cliente, _ = models.Cliente.objects.get_or_create(
            GLN=data["Inventario"]["Cliente"]["GLN_Cliente"])
        new_Sucursal, _ = models.Sucursal.objects.get_or_create(
            GLN=data["Inventario"]["Sucursal"]["GLN_Sucrusal"])
        new_Producto, _ = models.Producto.objects.get_or_create(GLN=data["Producto"]["Gtin_Producto"],
                                                                precio=data["Producto"]["PrecioUnidad"])
        new_Inventario = models.Inventario.objects.create(
            clienteFK=new_Cliente, sucursalFK=new_Sucursal, fecha=data["Inventario"]["Fecha"])
        new_Registro = models.Registro.objects.create(
            inventarioFK=new_Inventario, productoFK=new_Producto, cantidad=data["Inventario_Final"])
        new_Registro.save()
        #print(new_Registro)
        serializer = AllRegistroSerializer(new_Registro)
        return Response(serializer.data)
