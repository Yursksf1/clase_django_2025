from django.shortcuts import render
from myapp.models import Park, Historico_Poblacion

# Create your views here.

def giron(request):
    parques =  Park.objects.filter(city='GRN').all()
    mensaje = "Villa de los Caballeros y Monumento Nacional"
    print(parques)
    
    context = {
        "mensaje": mensaje,
        "parques": parques,
    }
    return render(request, "giron.html", context)


def bucaramanga(request):
    parques =  Park.objects.filter(city='BUC').all()
    history_poblations =  Historico_Poblacion.objects.all()
    print(parques)
    
    context = {
        "parques": parques,
        "history_poblations": history_poblations,
    }
    return render(request, "bucaramanga.html", context)