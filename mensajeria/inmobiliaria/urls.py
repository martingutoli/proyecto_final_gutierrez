from django.urls import path
from inmobiliaria.views import *
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path("", inicio, name = "inicio"),
    path("alquileres/", alquileres, name = "alquileres"),
    path("ventas/", ventas, name = "ventas"),
    path("about/", about, name = "about"),
    path("busqueda", form_busqueda, name = "busqueda"),
    path("resultados/", buscar, name = "resultado_busqueda"),
    path("login/", iniciar_sesion, name = "login"),
    path("registro/", registrar, name = "registro"),
    path("logout/", LogoutView.as_view(template_name = "inmobiliaria/logout.html"), name = "logout"),
    path("editar/", editar_usuario, name = "editar"),
    path("crear_inmueble/", crear_inmueble, name = "crear_inmueble"),
    #path("crear_inmueble2/", crear_inmueble2, name = "crear_inmueble"),
    path("borrar_inmueble/<id_inmueble>", borrar_inmueble, name = "borrar_inmueble"),
    path("editar_inmueble/<id_inmueble>", editar_inmueble, name = "editar_inmueble"),
    path("inmuebles/<pk>", InmueblesDetail.as_view(), name="inmuebles"),
    path("inmuebles/", InmueblesList.as_view(), name = "inmuebles"),
    
]
