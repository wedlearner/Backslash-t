from django.contrib import admin
from django.urls import path
from . import views
app_name = 'servicios'

urlpatterns = [
    path('', views.ver_servicios, name = 'ver_servicios'),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio')
]