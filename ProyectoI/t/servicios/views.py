from django.shortcuts import render
from .models import servicio
def ver_servicios(request):
    servicios = servicio.objects.all()
    return render (request, 'servicios/ver_servicios.html', {'servicios':servicios})
# Create your views here.
