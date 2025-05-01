import json

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from timeline.models import TimeLine
from timeline.forms import TimeLineForm

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


# Vista GET
def timeline_get_view(request):
    if request.GET:
        year = request.GET.get("year")
        name = request.GET.get("name")
        description = request.GET.get("description")
        return HttpResponse(f"GET Data: {year}, {name}, {description}")
    return render(request, "timeline_get.html")

# Vista POST
@csrf_exempt  # Solo para pruebas, no en producción
def timeline_post_view(request):
    if request.method == "POST":
        year = request.POST.get("year")
        name = request.POST.get("name")
        description = request.POST.get("description")

        timeline = TimeLine(year=year, name=name, description=description)
        timeline.save()
        
        return HttpResponse(f"POST Data: {year}, {name}, {description}")
    return render(request, "timeline_post.html")

# Vista usando TimeLineForm
def timeline_form_view(request):
    if request.method == "POST":
        form = TimeLineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Guardado correctamente")
    else:
        form = TimeLineForm()
    return render(request, "timeline_form.html", {'form': form})

# Vista basada en clase
class TimeLineFormView(FormView):
    template_name = "timeline_form.html"
    form_class = TimeLineForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)