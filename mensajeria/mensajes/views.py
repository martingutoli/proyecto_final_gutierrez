from mensajes.models import Contacto
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from mensajes.models import Contacto
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def crear_mensaje(request):
    return render (request, "mensajes/crear_mensaje.html")

class ContactoList(ListView):
    model = Contacto
    template_name = "mensajes/mensajes_list.html"

class ContactoCrear(CreateView):
    model = Contacto
    success_url = "mensajes/mensajes_list.html"
    fields = ["nombre", "mensaje"]