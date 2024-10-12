from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("change_groupe/PROCESS", views.change, name='change'),
    
]