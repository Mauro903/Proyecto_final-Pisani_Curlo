from django.urls import path
from Pagina_principal.views import *

urlpatterns = [
    path('', bienvenidos, name='bienvenidos'),
    path('peliculas/', PeliculasListView.as_view(), name='listar_peliculas'),
    path('blog/', blog, name='blog'),
    path('bienvenidos', bienvenidos, name='bienvenidos'),
    
]
