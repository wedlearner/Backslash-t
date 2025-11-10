from django.shortcuts import render, redirect, get_object_or_404
from .models import servicio
from django.contrib import messages

def ver_servicios(request):
    servicios = servicio.objects.all()
    return render (request, 'servicios/ver_servicios.html', {'servicios':servicios})
# Create your views here.
def agregar_servicio(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')

        nuevo_servicio = servicio.objects.create(
            titulo=titulo,
            trabajador = request.user.perfil,
            descripcion=descripcion,
            precio = precio
        )
        messages.success(request, 'Servicio agregado exitosamente')
        return redirect('ver_perfil')
    
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

def eliminar_servicio(request, servicio_id):
    serv = get_object_or_404(servicio, id=servicio_id)
    if serv.trabajador != request.user.perfil:
        return redirect('ver_perfil')
    serv.delete()
    return redirect('ver_perfil')
