from django.contrib import admin

from .models import  Temporada, Casa, Personaje

# Register your models here.
class TemporadaAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Datos de la temporada', {'fields':['num_temporada', 'num_episodios']}),
    ('Imagen de temporada', {'fields':['imagen']}),
    ]
    list_display = ('num_temporada', 'num_episodios')
    list_filter = ['num_episodios']

class CasaAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Datos de la casa', {'fields':['nombre', 'lema', 'asentamiento', 'num_personajes']}),
    ('Imagen de la casa', {'fields':['imagen']}),
    ]
    list_display = ('nombre', 'lema', 'asentamiento')
    search_fields = ['nombre']

class PersonajeAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Datos del personaje', {'fields':['nombre', 'casa', 'temporadas']}),
    ('Descripcion del personaje', {'fields':['descripcion']}),
    ('Imagen del personaje', {'fields':['imagen']}),
    ]
    list_display = ('nombre', 'casa')
    list_filter = ['casa']
    search_fields = ['nombre']

admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Casa, CasaAdmin)
admin.site.register(Temporada, TemporadaAdmin)
