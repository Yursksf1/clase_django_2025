from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje = "Villa de los Caballeros y Monumento Nacional 1111"
    parques = [
        {
            "name": "Parque Pincipal",
            "description": "Parque en el centro de giron con la iglesia principal"
        },
        {
            "name": "Parque las nieves",
            "description": "Parque con la iglesia de las nieves"
        },
        {
            "name": "Parque peralta",
            "description": "Parque mas tranquilo y se pueden comprar deliciosos helados!"
        },
    ]
    print(parques)
    
    context = {
        "mensaje": mensaje,
        "parques": parques,
    }
    return render(request, "giron.html", context)