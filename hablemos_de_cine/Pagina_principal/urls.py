from django.urls import path
from Pagina_principal.views import *

urlpatterns = [
    path('bienvenidos/', bienvenidos, name='bienvenidos'),
    
]
