from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from task_app.models import Task


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    print(request.POST)
    task_data = {
        'desc': request.POST.get('desc'),
        'status': request.POST.get('status'),
        'date': request.POST.get('date'),
        'author': request.POST.get('author')
    }
    task = Task.objects.create(**task_data)
    return redirect(f'/task/?pk={task.pk}')

def detail_view(request):
    task_pk = request.GET.get('pk')
    task = Task.objects.get(pk=task_pk)
    context = {'task': task}
    return render(request, 'task.html', context=context)