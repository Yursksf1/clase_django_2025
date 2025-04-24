from django.urls import path
from django.views.generic import TemplateView
from timeline import views

urlpatterns = [
    path('disney/',views.timeline),
]