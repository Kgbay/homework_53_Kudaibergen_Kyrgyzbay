from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    context = {
        'desc': request.POST.get('desc'),
        'status': request.POST.get('status'),
        'date': request.POST.get('date')
    }
    return render(request, 'task.html', context=context)