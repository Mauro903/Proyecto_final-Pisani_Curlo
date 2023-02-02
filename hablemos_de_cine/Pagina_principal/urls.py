from django.urls import path
from Pagina_principal.views import *
from login.views import *
urlpatterns = [
    path('', bienvenidos, name='bienvenidos'),
    path('peliculas/', PeliculasListView.as_view(), name='listar_peliculas'),
    path('blog/', blog, name='blog'),
    path('bienvenidos', bienvenidos, name='bienvenidos'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
]
