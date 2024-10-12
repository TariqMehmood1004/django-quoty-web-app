from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='details/', view=views.details, name='details'),
    path(route='pay/', view=views.pay, name='pay'),
    path(route='contact/', view=views.contact, name='contact'),
]
