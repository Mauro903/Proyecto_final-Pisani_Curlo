from django.shortcuts import render

# Create your views here.


def bienvenidos(request):
        return render(
        template_name="Pagina_principal/inicio.html",
    )