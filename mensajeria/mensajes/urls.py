from django.urls import path
from mensajes.views import *

urlpatterns = [
    path ("", crear_mensaje),
    path ("mensajes/", ContactoList.as_view(), name = "mensajes"),
    path ("mensajes/crear", ContactoCrear.as_view(), name = "mensajes/crear"),
]
