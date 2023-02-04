
from Pagina_principal.models import *
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Categoria, Web, Suscriptor
import random
from .utils import *
from .form import ContactoForm
from django.core.mail import send_mail
from hablemos_de_cine.settings import EMAIL_HOST_USER

# Create your views here.


def inicio(request):
        return render(
        request=request,
        template_name="Pagina_principal/inicio.html",)


class Blog(ListView):
        
        def get(self,request,*args,**kwargs):
            posts = list(Post.objects.filter(
                    estado = True,
                    publicado = True
                    ).values_list("id",flat = True))
            principal = random.choice(posts)
            posts.remove(principal)
            principal = consulta(principal)
            
            post1 = random.choice(posts)
            posts.remove(post1)
            post2 = random.choice(posts)
            posts.remove(post2)
            post3 = random.choice(posts)
            posts.remove(post3)
            post4 = random.choice(posts)
            posts.remove(post4)

            try:
                post_peliculas = Post.objects.filter(
                                  estado = True,
                                  publicado = True,
                                  categoria = Categoria.objects.get(nombre = 'peliculas')
                                  ).latest('fecha_publicacion')
            except:
                post_peliculas = None

            try:
                post_series = Post.objects.filter(
                               estado = True,
                               publicado = True,
                               categoria = Categoria.objects.get(nombre = 'series')
                               ).latest('fecha_publicacion')
            except:
                post_series = None

            contexto = {
                "principal": principal,
                'post1': consulta(post1),
                'post2': consulta(post2),
                'post3': consulta(post3),
                'post4': consulta(post4),
                'post_series':post_series,
                'post_peliculas':post_peliculas,
                'sociales':obtenerRedes(), 
                'web':obtenerWeb(),
            }
            
            return render(request,"Pagina_principal\Blog.html",contexto)
        

class DetallePost(DetailView):
    def get(self,request,slug,*args,**kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)

        contexto = {
            'post':post,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),
        }
        return render(request,'Pagina_principal\post.html',contexto,)
    


    
class Listado(ListView):

    def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        return render(request,'Pagina_principal\categoria.html',contexto,)
    


class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,
        }
        return render(request,'Pagina_principal\contacto.html',contexto,)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contacto.html',contexto,)    
        
class Suscribir(View):
    def post(self,request,*args,**kwargs):
        correo = request.POST.get('correo')
        Suscriptor.objects.create(correo = correo)
        asunto = 'GRACIAS POR SUSCRIBIRTE A Hablemos de CINE!'
        mensaje = 'Te haz suscrito exitosamente a Hablemos de CINE, Gracias por elegirnos!!!'
        try:
            send_mail(asunto,mensaje,EMAIL_HOST_USER,[correo])
        except:
            pass

        return redirect('inicio')
