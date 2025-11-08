from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from difflib import SequenceMatcher
from .models import servicio


def ver_servicios(request):
    """Lista servicios y, si hay query `q`, filtra y ordena por similitud.

    - Parámetros GET: q (texto de búsqueda)
    - Búsqueda: aplica icontains sobre titulo, trabajador y descripcion
    - Orden: calcula un ratio de similitud (difflib) entre la query y los campos y ordena descendente
    """
    q = request.GET.get('q', '').strip()

    if q:
        # filtrado básico con icontains
        qs = servicio.objects.filter(
            Q(titulo__icontains=q) | Q(trabajador__icontains=q) | Q(descripcion__icontains=q)
        ).distinct()

        # calcular similitud y ordenar en Python (sqlite no tiene trigram por defecto)
        def score(srv):
            # Compara la query con cada campo y devuelve el máximo de similitud
            t = (srv.titulo or '')
            tr = (srv.trabajador or '')
            d = (srv.descripcion or '')
            ratios = []
            for field in (t, tr, d):
                try:
                    ratios.append(SequenceMatcher(None, q.lower(), field.lower()).ratio())
                except Exception:
                    ratios.append(0)
            return max(ratios)

        servicios_list = list(qs)
        servicios_list.sort(key=score, reverse=True)
        servicios = servicios_list
    else:
        servicios = servicio.objects.all()

    return render(request, 'servicios/ver_servicios.html', {'servicios': servicios, 'q': q})
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