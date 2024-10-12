from django.urls import path

from . import views


urlpatterns = [
    path("", views.welcome, name='welcome'),
    path("change_groupe/", views.index, name='index'),
    path("change_groupe/PROCESS", views.change, name='change'),
    
]