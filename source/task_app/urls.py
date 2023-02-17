from django.urls import path

from .views.base import index_view
from .views.tasks import add_view, detail_view, remove_view

urlpatterns = [
    path("", index_view),
    path("task/add/", add_view),
    path('task/<int:pk>', detail_view, name='detail_view'),
    path("rm/", remove_view)
]