from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from task_app.models import Task


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    task_data = {
        'desc': request.POST.get('desc'),
        'status': request.POST.get('status'),
        'date': request.POST.get('date'),
        'author': request.POST.get('author')
    }
    task = Task.objects.create(**task_data)
    return redirect('detail_view', pk = task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })



def remove_view(request):
    task_pk = request.GET.get('pk')
    task = Task.objects.get(pk=task_pk)
    context = {'task': task}
    removal = task.delete()
    return render(request, 'remove.html', context=context)
