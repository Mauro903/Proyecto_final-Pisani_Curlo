from django.urls import path
from Pagina_principal.views import *
from login.views import *
urlpatterns = [
    path('', bienvenidos, name='bienvenidos'),
   #path('peliculas/', PeliculasListView.as_view(), name='listar_peliculas'),
    path('blog/', Blog.as_view(), name='blog'),
    path('bienvenidos', bienvenidos, name='bienvenidos'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
    path('peliculas/',Listado.as_view(),{'nombre_categoria':'peliculas'}, name = 'peliculas'),
    path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
    path('series/',Listado.as_view(),{'nombre_categoria':'series'}, name = 'series'),
] 
