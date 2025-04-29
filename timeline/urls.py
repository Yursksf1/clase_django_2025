from django.urls import path
from django.views.generic import TemplateView
from timeline import views

urlpatterns = [
    path('disney/',views.timeline),
    path('api/peliculas/', views.crear_pelicula, name='crear_pelicula')
]