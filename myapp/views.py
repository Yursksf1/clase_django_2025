from django.shortcuts import render
from myapp.models import Park

# Create your views here.

def index(request):
    parques =  Park.objects.all()
    mensaje = "Villa de los Caballeros y Monumento Nacional"
    print(parques)
    
    context = {
        "mensaje": mensaje,
        "parques": parques,
    }
    return render(request, "giron.html", context)