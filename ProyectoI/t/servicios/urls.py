from django.contrib import admin
from django.urls import path
from . import views
app_name = 'servicios'

urlpatterns = [
    path('', views.ver_servicios, name = 'ver_servicios'),
    path('', views.ver_servicios, name='ver_servicios'),
    path('agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio')
]
