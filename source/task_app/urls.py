from django.urls import path

from task_app.views.base import index_view
from task_app.views.tasks import add_view

urlpatterns = [
    path("", index_view),
    path("task/add", add_view)
]