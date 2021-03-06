
from django.contrib import admin
from django.urls import path
from .import views
app_name = "Inventario_app"
urlpatterns = [
    path('api/AllRegistro/', views.ListAllRegistroView.as_view(),name="listCompleteRegistro"),
    path('api/Inventario/', views.ListInventarioView.as_view(),name="listInventario"),
    path('api/Registro/', views.ListRegistroView.as_view(),name="listRegistro"),
    path('api/CreateRegistro/', views.CreateRegistroView.as_view(),name="listCreateRegistro"),
    path('api/UpdateRegistro/', views.UpdateRegistroView.as_view(),name="listUpdateRegistro"),
    path('api/AllRegistro/byCliente/<GLN_cliente>/', views.ListRegistrobyClienteView.as_view(),name="listCompleteRegistrobyCliente"),
    path('api/AllRegistro/bySucursal/<GLN_Sucursal>/', views.ListRegistrobySucursalView.as_view(),name="listCompleteRegistrobySucursal"),
    path('api/AllRegistro/byProducto/<GLN_Producto>/', views.ListRegistrobyProductoView.as_view(),name="listCompleteRegistrobyProducto")    
]
