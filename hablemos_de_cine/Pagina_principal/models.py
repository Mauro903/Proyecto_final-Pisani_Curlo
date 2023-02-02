from django.db import models




class Peliculas(models.Model):
    titulo = models.CharField(max_length=30)
    duracion = models.CharField(max_length=10)
    director = models.CharField(max_length=30)
    fecha_estreno = models.DateField(null=True)
    clasificación = models.CharField(max_length=50)

class Series(models.Model):
    titulo = models.CharField(max_length=30)
    duracion = models.CharField(max_length=10)
    director = models.CharField(max_length=30)
    fecha_estreno = models.DateField(null=True)
    clasificación = models.CharField(max_length=50)

# Create your models here.
