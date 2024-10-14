from django.contrib import admin
from django.urls import path
from . import views 
from .views import add_trails, trails

urlpatterns = [
    path('', views.trails, name='trails'),
    path('add', add_trails, name='add_trail')
]