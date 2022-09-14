from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from inmobiliaria.models import Inmuebles #Alquileres, Ventas #Avatar
from django.contrib.auth.forms import AuthenticationForm
from inmobiliaria.forms import UserCustomCreationForm, UserCreationForm, UserEditForm, InmueblesFormulario
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):

    #context= {
     #   "mensaje": "hola"
    #}
    #if not request.user.is_anonymous:
     #   avatar = Avatar.objects.filter(usuario = request.user ).last()
      #  context.update({"avatar": avatar})

    listado_inmuebles = Inmuebles.objects.all()

    return render (request, "inmobiliaria/index.html", {"inmuebles": listado_inmuebles})

#@login_required
def alquileres(request):
   
    listado_inmuebles = Inmuebles.objects.filter(tipo_de_operacion = 'Alquiler')

    return render (request, "inmobiliaria/alquileres.html", {"inmuebles": listado_inmuebles})

def ventas(request):

    listado_inmuebles = Inmuebles.objects.filter(tipo_de_operacion = 'Venta')

    return render(request, "inmobiliaria/ventas.html", {"inmuebles": listado_inmuebles})

def about(request):
    return render(request, "inmobiliaria/about.html")

def form_busqueda(request):
    return render(request, "inmobiliaria/form_busqueda.html")

def buscar (request):
    inmueble_tipo = request.GET.get('descripcion', None)

    if not inmueble_tipo:
        return HttpResponse ("No indicaste nada")
    inmuebles_lista = Inmuebles.objects.filter(descripcion__icontains=inmueble_tipo)
    return render(request, "inmobiliaria/resultado_busqueda.html", {"inmuebles": inmuebles_lista})

def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        context ={

            "form" : formulario
        }

        return render(request, "inmobiliaria/login.html", context)
    else:
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login  (request, usuario)
                return redirect("inicio")
            else:
                context = {
                    "error" : "Credenciales no validas",
                    "form" : formulario
                }
                
                return render(request, "inmobiliaria/login.html", context)
        else:

            context = {
                    "error" : "Formulario no valido",
                    "form" : formulario
            }
                
            return render(request, "inmobiliaria/login.html", context)

    return HttpResponse()

def registrar(request):

    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request, "inmobiliaria/registro.html", {"form": formulario})
    else:
        formulario = UserCustomCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request, "inmobiliaria/registro.html", {"form": formulario, "error": "Formulario no valido"})

@login_required
def editar_usuario(request):


    if request.method == "GET":
        form = UserEditForm(initial={"email": request.user.email,"first_name": request.user.first_name, "last_name": request.user.last_name})
        return render(request, "inmobiliaria/editar_usuario.html", {"form": form})

    else:
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = request.user

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()
            return redirect('inicio')
        else:
            return render(request, 'inmobiliaria/editar_usuario.html', {"form" : form})

def crear_inmueble(request):
    if request.method == "GET":
        return render(request, "inmobiliaria/crear_inmueble.html")
    else:
        tipo_de_operacion = request.POST["tipo_de_operacion"]
        precio = request.POST["precio"]
        cantidad_ambientes = request.POST["cantidad_ambientes"]
        cantidad_dormitorios = request.POST["cantidad_dormitorios"]
        descripcion = request.POST["descripcion"]
        inmueble = Inmuebles(tipo_de_operacion = tipo_de_operacion, precio=precio, cantidad_ambientes=cantidad_ambientes, cantidad_dormitorios=cantidad_dormitorios, descripcion=descripcion)
        inmueble.save()
        return render(request, "inmobiliaria/index.html")

#def crear_inmueble2(request):
#    if request.method == "GET":
 #       return render(request, "inmobiliaria/crear_inmueble.html")
  #  else:
   #     tipo_de_operacion = request.POST["tipo_de_operacion"]
    #    precio = request.POST["precio"]
     #   cantidad_ambientes = request.POST["cantidad_ambientes"]
      #  cantidad_dormitorios = request.POST["cantidad_dormitorios"]
       # descripcion = request.POST["descripcion"]
        #inmueble = Ventas(tipo_de_operacion = tipo_de_operacion, precio=precio, cantidad_ambientes=cantidad_ambientes, cantidad_dormitorios=cantidad_dormitorios, descripcion=descripcion)
        #inmueble.save()
        #return render(request, "inmobiliaria/index.html")

def borrar_inmueble(request, id_inmueble):
    try:
        inmueble = Inmuebles.objects.get(id=id_inmueble)
        inmueble.delete()
        return redirect("inicio")
    except:
        return redirect("inicio")

#def borrar_inmueble2(request, id_inmueble):
 #   try:
  #      inmueble = Ventas.objects.get(id=id_inmueble)
   #     inmueble.delete()
    #    return redirect("ventas")
    #except:
     #   return redirect("inicio")

def editar_inmueble(request, id_inmueble):
    if request.method == "GET":
        formulario = InmueblesFormulario()
        contexto = {

            "formulario": formulario
        }
        return render(request, "inmobiliaria/crear_inmueble.html", contexto)
    else:
        formulario =InmueblesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                inmueble = Inmuebles.objects.get(id=id_inmueble)

                inmueble.tipo_de_operacion = data.get("tipo_de_operacion")
                inmueble.precio = data.get("precio")
                inmueble.cantidad_ambientes = data.get("cantidad_ambientes")
                inmueble.cantidad_dormitorios = data.get("cantidad_dormitorios")
                inmueble.descripcion = data.get("descripcion")
                inmueble.save()
                
            except:
                return HttpResponse("Error en la actualizacion")
            
        return redirect("inicio")

class InmueblesList( ListView):
    model = Inmuebles
    template_name = "inmobiliaria/inmuebles_list.html"

    def alqui(request):
        listado_inmuebles = Inmuebles.objects.filter(tipo_de_operacion = 'Alquiler')

        return render (request, "inmobiliaria/alquileres.html", {"inmuebles": listado_inmuebles})

        

class InmueblesDetail(DetailView):
    model = Inmuebles
    template_name = "inmobiliaria/alquileres_detail.html"

    