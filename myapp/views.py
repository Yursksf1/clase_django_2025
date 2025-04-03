from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje = "Villa de los Caballeros y Monumento Nacional 12345"
    parques = [
        "Parque Pincipal",
        "Parque las nieves",
        "Parque peralta"
    ]
    print(parques)
    
    context = {
        "mensaje": mensaje,
        "parques": parques,
    }
    return render(request, "giron.html", context)