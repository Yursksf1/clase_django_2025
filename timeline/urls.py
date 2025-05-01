from django.urls import path
from django.views.generic import TemplateView
from timeline import views

urlpatterns = [
    path('disney/',views.timeline),
    path('api/peliculas/', views.crear_pelicula, name='crear_pelicula'),
    
    path("timeline/get/", views.timeline_get_view, name="timeline_get"),
    path("timeline/post/", views.timeline_post_view, name="timeline_post"),
    path("timeline/form/", views.timeline_form_view, name="timeline_form"),
    path("timeline/class/", views.TimeLineFormView.as_view(), name="timeline_class"),
]