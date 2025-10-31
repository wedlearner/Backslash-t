from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
from .models import servicio

def ver_servicios(request):
    servicios = servicio.objects.all()
    return render (request, 'servicios/ver_servicios.html', {'servicios':servicios})
# Create your views here.
def agregar_servicio(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        trabajador = request.POST.get('trabajador')
        descripcion = request.POST.get('descripcion')
        
        nuevo_servicio = servicio.objects.create(
            titulo=titulo,
            trabajador=trabajador,
            descripcion=descripcion
        )
        messages.success(request, 'Servicio agregado exitosamente')
        return redirect('ver_servicios')
    
    return render(request, 'servicios/agregar_servicio.html')

def editar_servicio(request, servicio_id):
    servicio_obj = get_object_or_404(servicio, id=servicio_id)
    
    if request.method == 'POST':
        servicio_obj.titulo = request.POST.get('titulo')
        servicio_obj.trabajador = request.POST.get('trabajador')
        servicio_obj.descripcion = request.POST.get('descripcion')
        servicio_obj.save()
        
        messages.success(request, 'Servicio actualizado exitosamente')
        return redirect('ver_servicios')
    
    return render(request, 'servicios/editar_servicio.html', {'servicio': servicio_obj})