from django.shortcuts import render
from todo_project.models import Task

# Create your views here.

def todo_list(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "task_list.html", context)

def todo_create(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "task_create.html", context)


def todo_list_create(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "task_list_create.html", context)

