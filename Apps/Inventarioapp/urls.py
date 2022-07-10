
from django.contrib import admin
from django.urls import path
from .import views
app_name = "Inventario_app"
urlpatterns = [
    path('api/Inventario/', views.ListInventarioView.as_view(),name="listInventario"),
    path('api/Registro/', views.ListRegistroView.as_view(),name="listRegistro"),
    path('api/AllRegistro/', views.ListAllRegistroView.as_view(),name="listCompleteRegistro"),
    path('api/CreateRegistro/', views.CreateRegistroView.as_view(),name="listCreateRegistro"),
]
