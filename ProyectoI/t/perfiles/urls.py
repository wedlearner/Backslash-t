from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('perfiles/', views.ver_perfil, name = 'ver_perfil')
]