from django.shortcuts import render
from timeline.models import TimeLine

# Create your views here.

def timeline(request):
    timeline_list =  TimeLine.objects.all()
    context = {
        "timeline_list": timeline_list,
    }
    return render(request, "linea_tiempo.html", context)