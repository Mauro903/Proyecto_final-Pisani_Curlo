from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from login.forms import *
# Create your views here.


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('bienvenidos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='login/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('bienvenidos')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='login/login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
    template_name = 'login/logout.html'