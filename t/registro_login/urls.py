from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name = 'index'),
path('login/', views.login_usuario, name = 'login'),
path('logout/', views.logout_usuario, name = 'logout'),
path('inicio/', views.inicio, name = 'inicio'),
path('registro/',views.registro, name = 'registro'),
]