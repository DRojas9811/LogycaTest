from django.contrib import admin
from django.urls import path
from . import views

app_name = "Informacion_app"
urlpatterns = [
    path('api/Cliente/', views.ListClienteView.as_view(), name="listCliente"),
    path('api/Sucursal/', views.ListSucursalView.as_view(), name="listSucursal"),
    path('api/Producto/', views.ListProductoView.as_view(), name="listProducto"),
    path('', views.indezView.as_view(), name='index'),
        
]
