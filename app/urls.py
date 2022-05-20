from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('tienda', tienda, name="tienda"),
    path('nosotros', nosotros, name="nosotros"),
    path('ubicacion', ubicacion, name="ubicacion"),
    path('repuestos', repuestos, name="repuestos"),
    path('cuerda', cuerda, name="cuerda"),
    path('percusion', percusion, name="percusion"),
    path('amplificadores', amplificadores, name="amplificadores"),
    path('inicio_sesion', inicio_sesion, name="inicio_sesion"),
    path('registro', registro, name="registro"),
    path('carrito', carrito, name="carrito"),
]