from django.urls import path
from . import views

urlpatterns = [
    path(path='', view=views.index, name='index'),
]
