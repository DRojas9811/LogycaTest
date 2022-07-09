
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('Inventario/', views.ListInventarioView.as_view()),
    path('Registro/', views.ListRegistroView.as_view()),
    path('AllRegistro/', views.ListAllRegistroView.as_view()),
    path('CreateRegistro/', views.CreateRegistroView.as_view()),
]
