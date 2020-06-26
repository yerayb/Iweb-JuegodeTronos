from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    path('personaje/<int:pk>/', views.personaje_detail, name='personaje_detail'),
    path('personaje/', views.personaje, name='personaje'),
    path('casa/<int:pk>/', views.casa_detail, name='casa_detail'),
    path('casa/', views.casa, name='casa'),
    path('temporada/', views.temporada, name='temporada'),
    path('temporada/<int:pk>', views.temporada_detail, name='temporada_detail'),
]
