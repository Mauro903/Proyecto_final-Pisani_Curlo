from django.urls import path
from login.views import *
from Pagina_principal.views import bienvenidos

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

]