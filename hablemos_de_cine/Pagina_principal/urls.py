from django.urls import path
from login.views import *
from Pagina_principal.views import *
from login.urls import agregaravatar







urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('', Blog.as_view(), name='blog'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('peliculas/',Listado.as_view(),{'nombre_categoria':'peliculas'}, name = 'peliculas'),
    path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
    path('series/',Listado.as_view(),{'nombre_categoria':'series'}, name = 'series'),
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
    path('agregar-avatar/', agregaravatar, name='agregar_avatar'),
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    
    
] 
