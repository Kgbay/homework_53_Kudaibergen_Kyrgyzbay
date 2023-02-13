from django.urls import path

from .views.base import index_view
from .views.tasks import add_view, detail_view

urlpatterns = [
    path("", index_view),
    path("task/add", add_view),
    path('task/', detail_view)
]