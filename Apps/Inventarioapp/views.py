from django.shortcuts import get_object_or_404
from Apps.Informacionapp.models import Cliente, Producto, Sucursal
from .serializers import (AllRegistroSerializer, InventarioPagination,
                          InventarioSerializer,
                          RegistroSerializer,
                          AllRegistroSerializer,
                          )
from .models import Inventario, Registro
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
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
        new_Cliente,_ = Cliente.objects.get_or_create(
            GLN=data["Inventario"]["Cliente"]["GLN_Cliente"])
        print(new_Cliente)
        new_Sucursal,_= Sucursal.objects.get_or_create(
            GLN=data["Inventario"]["Sucursal"]["GLN_Sucrusal"])
        print(new_Sucursal)
        new_Producto,_ = Producto.objects.get_or_create(GLN=data["Producto"]["Gtin_Producto"],
                                                                precio=data["Producto"]["PrecioUnidad"])
        print(new_Producto)
        try:
            new_Registro= Registro.objects.get(productoFK__GLN=new_Producto.GLN, 
                                                        inventarioFK__clienteFK__GLN=new_Cliente.GLN,
                                                        inventarioFK__sucursalFK__GLN=new_Sucursal.GLN)
            print(new_Registro)
        except Exception as e:
            print(e)
            new_Inventario,_ = Inventario.objects.get_or_create(clienteFK=new_Cliente, sucursalFK=new_Sucursal, fecha=data["Inventario"]["Fecha"])
            print(new_Inventario)
            new_Registro = Registro.objects.create(inventarioFK=new_Inventario, productoFK=new_Producto, cantidad=data["Inventario_Final"])
            new_Registro.save()          
            #print(new_Registro)
            serializer = AllRegistroSerializer(new_Registro)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print("Registro exists, please use PUT Request to update Registro.")
            serializer = AllRegistroSerializer(new_Registro)
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)


class UpdateRegistroView(UpdateAPIView):

    serializer_class =AllRegistroSerializer
    def get_object(self):
        data = self.request.data
        new_Cliente = data["Inventario"]["Cliente"]["GLN_Cliente"]
        new_Sucursal= data["Inventario"]["Sucursal"]["GLN_Sucrusal"]
        new_Producto = [data["Producto"]["Gtin_Producto"],data["Producto"]["PrecioUnidad"]]
        new_Registro= get_object_or_404(Registro,productoFK__GLN=new_Producto[0], 
                                                    inventarioFK__clienteFK__GLN=new_Cliente,
                                                    inventarioFK__sucursalFK__GLN=new_Sucursal)
        print(new_Registro)
        return new_Registro

    def put(self,request):
        new_Registro=self.get_object()
        data=self.request.data
        new_Cliente,_ = Cliente.objects.get_or_create(
            GLN=data["Inventario"]["Cliente"]["GLN_Cliente"])
        ##print(new_Cliente)
        new_Sucursal,_= Sucursal.objects.get_or_create(
            GLN=data["Inventario"]["Sucursal"]["GLN_Sucrusal"])
       ## print(new_Sucursal)
        new_Producto,_ = Producto.objects.get_or_create(GLN=data["Producto"]["Gtin_Producto"],
                                                                precio=data["Producto"]["PrecioUnidad"])

        new_Inventario=Inventario.objects.get(clienteFK__GLN=new_Cliente.GLN,
                                                        sucursalFK__GLN=new_Sucursal.GLN)
        new_Inventario.fecha=data["Inventario"]["Fecha"]
        new_Inventario.save()
        new_Registro.inventarioFK,new_Registro.productoFK,new_Registro.cantidad = new_Inventario,new_Producto, data["Inventario_Final"]
        new_Registro.save()
        return Response(status=status.HTTP_202_ACCEPTED)

