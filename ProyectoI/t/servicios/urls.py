from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_servicios, name = 'ver_servicios')

]