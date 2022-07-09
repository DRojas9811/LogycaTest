from multiprocessing.connection import Client
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
)
from .serializers import ClienteSerializer, ProductoSerializer, SucursalSerializer
# Create your views here.
from .models import Cliente, Producto, Sucursal


def index(request):
    print('Request for index page received')
    return render(request, 'Informacionapp/index.html')


class ListClienteView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.ListCliente()


class ListSucursalView(ListAPIView):
    serializer_class = SucursalSerializer

    def get_queryset(self):
        return Sucursal.objects.ListSucursal()


class ListProductoView(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.ListProducto()
