from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Casa(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.URLField('imagen', max_length=225, blank=False, null=False)
    lema = models.TextField()
    asentamiento = models.CharField(max_length=40)
    num_personajes = models.IntegerField()

    def __str__(self):
        return self.nombre


class Temporada(models.Model):
    num_temporada = models.IntegerField()
    num_episodios = models.IntegerField()
    imagen = models.URLField('imagen', max_length=225, blank=False, null=False)


    def __str__(self):
        return "Temporada " + str(self.num_temporada)

class Personaje(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = RichTextField('Descripcion')
    imagen = models.URLField('imagen', max_length=225, blank=False, null=False)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE,related_name='casaPersona')
    temporadas = models.ManyToManyField('Temporada',related_name='tempo')


    def __str__(self):
        return self.nombre