from django.contrib import admin
from django.urls import path
from . import views

app_name = "Informacion_app"
urlpatterns = [
    path('Cliente/', views.ListClienteView.as_view(), name="listClient"),
    path('Sucursal/', views.ListSucursalView.as_view(), name="listSucursal"),
    path('Producto/', views.ListProductoView.as_view(), name="listProducto"),
        
]
