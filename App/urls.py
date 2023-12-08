
from django.urls import path
from App.views import home, agregar_categoria, agregar_producto, agregar_cliente, buscar

urlpatterns = [
    path('' , home, name='home'),
    path('agregar_categoria/', agregar_categoria, name='agregar_categoria'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('buscar/', buscar, name='buscar'),
    

]
