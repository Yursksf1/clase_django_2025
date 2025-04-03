from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje = "Villa de los Caballeros y Monumento Nacional 12345"
    context = {
        "mensaje": mensaje
    }
    return render(request, "giron.html", context)