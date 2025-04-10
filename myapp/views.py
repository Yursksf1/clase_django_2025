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
    history_poblations_list = []
    history_poblations =  Historico_Poblacion.objects.order_by("year").all()
    ratio_growth = None
    previous_poblation = history_poblations[0]
    for history_poblation in history_poblations:
        if previous_poblation.year != history_poblation.year:
            ratio_growth = round((history_poblation.poblation / previous_poblation.poblation -1), 2)
            previous_poblation = history_poblation
        history_poblations_list.append(
            {
                "year": history_poblation.year,
                "poblation": history_poblation.poblation,
                "ratio_growth": ratio_growth,
            }
        )


    print(parques)
    
    context = {
        "parques": parques,
        "history_poblations": history_poblations_list,
    }
    return render(request, "bucaramanga.html", context)