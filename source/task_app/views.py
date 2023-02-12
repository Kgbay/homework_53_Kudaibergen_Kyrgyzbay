from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
def index_view(request: WSGIRequest):
    return render(request, 'index.html')
