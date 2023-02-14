from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from task_app.models import Task


# Create your views here.
def index_view(request: WSGIRequest):
    # status_list = [('new', 'новый'), ('in process', 'в процессе'), ('done', 'сделано')]
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)