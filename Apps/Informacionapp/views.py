from multiprocessing.connection import Client
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
)
from django.templatetags.static import static
from django.views.generic import TemplateView
from .serializers import ClienteSerializer, InfoPagination, ProductoSerializer, SucursalSerializer
# Create your views here.
from .models import Cliente, Producto, Sucursal


class indexView(TemplateView):
    template_name ="Informacionapp/index.html"
class docsView(TemplateView):
    template_name ="Informacionapp/docs.html"
class ListClienteView(ListAPIView):
    serializer_class = ClienteSerializer
    pagination_class= InfoPagination

    def get_queryset(self):
        return Cliente.objects.ListCliente()


class ListSucursalView(ListAPIView):
    serializer_class = SucursalSerializer
    pagination_class= InfoPagination

    def get_queryset(self):
        return Sucursal.objects.ListSucursal()


class ListProductoView(ListAPIView):
    serializer_class = ProductoSerializer
    pagination_class= InfoPagination

    def get_queryset(self):
        return Producto.objects.ListProducto()
