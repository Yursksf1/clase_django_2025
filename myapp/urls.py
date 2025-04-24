

from django.urls import path
from django.views.generic import TemplateView
from myapp import views

urlpatterns = [
    path('bucaramanga/',views.bucaramanga),
    path('floridablanca/', TemplateView.as_view(template_name='floridablanca.html')),
    path('giron/', views.giron)
]