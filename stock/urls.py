from django.urls import path
from stock.views import crear_pantalon, crear_remera, crear_buzo

urlpatterns = [
    path("crear_pantalon/",crear_pantalon, name= "crear_pantalon" ),
    path("crear_remera/", crear_remera, name = "crear_remera"),
    path("crear_buzo/",crear_buzo, name = "crear_buzo" )
]