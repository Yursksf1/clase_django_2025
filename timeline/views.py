from django.shortcuts import render
from timeline.models import TimeLine
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

def timeline(request):
    timeline_list =  TimeLine.objects.all()
    context = {
        "timeline_list": timeline_list,
    }
    return render(request, "linea_tiempo.html", context)

@csrf_exempt
def crear_pelicula(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        timeline = TimeLine()
        timeline.year = int(data['year'])
        timeline.name = data['name']
        timeline.description = data['description']
        timeline.save()
        return JsonResponse({'id': timeline.id, 'titulo': timeline.name})

    else:
        return JsonResponse({})
