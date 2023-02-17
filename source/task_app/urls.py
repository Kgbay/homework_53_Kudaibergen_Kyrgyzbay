from django.urls import path

from .views.base import index_view
from .views.tasks import add_view, detail_view, remove_view

urlpatterns = [
    path("", index_view, name='index'),
    path("task/add/", add_view, name="article_add"),
    path('task/<int:pk>', detail_view, name='detail_view'),
    path("rm/", remove_view, name='remove_view')
]