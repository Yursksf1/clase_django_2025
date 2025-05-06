from django.urls import path
from django.views.generic import TemplateView
from todo_project import views

urlpatterns = [
    path('', views.todo_list),
    path('create/', views.todo_create),
    path('list_create/', views.todo_list_create),
]