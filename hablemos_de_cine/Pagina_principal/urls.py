from django.urls import path
from login.views import *
from .views import *






urlpatterns = [
    path("", bienvenidos, name='bienvenidos' ),
    path('bienvenidos/', bienvenidos, name='bienvenidos'),
    path('', Blog.as_view(), name='blog'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('peliculas/',Listado.as_view(),{'nombre_categoria':'peliculas'}, name = 'peliculas'),
    #path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
    path('series/',Listado.as_view(),{'nombre_categoria':'series'}, name = 'series'),
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
] 
