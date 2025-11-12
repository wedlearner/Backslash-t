from django.contrib import admin
from django.urls import path
from . import views

app_name = 'perfiles'

urlpatterns = [
    path('ver_perfil/', views.ver_perfil, name = 'ver_perfil'),
    path('editar_perfil/',views.editar_perfil, name = 'editar_perfil'),
    path('tutorial/', views.tutorial, name= 'tutorial'),
    path('tutorial_sesionIniciada/', views.tutorial_sesionIniciada, name= 'tutorial_sesionIniciada'),

]