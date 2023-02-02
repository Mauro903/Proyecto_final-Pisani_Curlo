
from Pagina_principal.models import *
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def bienvenidos(request):
        return render(
        request=request,
        template_name="Pagina_principal/inicio.html",
    )
def blog(request):
        return render(
        request=request,
        template_name="Pagina_principal/Blog.html",
    )

class PeliculasListView(LoginRequiredMixin, ListView):
    model = Peliculas
    template_name = "Pagina_principal/lista_peliculas.html"