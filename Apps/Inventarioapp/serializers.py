from unicodedata import name
from Apps.Informacionapp.models import Producto
from .models import Inventario, Registro
from rest_framework import serializers, pagination
from ..Informacionapp.serializers import ProductoSerializer, SucursalSerializer, ClienteSerializer


class InventarioSerializer(serializers.Serializer):
    Cliente = ClienteSerializer(source="clienteFK")
    Sucursal = SucursalSerializer(source="sucursalFK")
    Fecha = serializers.DateField(source='fecha')


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = "__all__"


class AllRegistroSerializer(serializers.Serializer):

    Inventario = InventarioSerializer(source="inventarioFK")
    Producto = ProductoSerializer(source="productoFK")
    Inventario_Final = serializers.IntegerField(source="cantidad")


class RegistroPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100
