from django.shortcuts import render,redirect
from .models import Perfil
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm

@login_required
def ver_perfil(request):
    perfil = request.user.perfil
    publicaciones = perfil.servicio_set.all()  
    return render(request, 'perfiles/perfil.html', {
        'perfil': perfil,
        'publicaciones': publicaciones
    })


@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == "POST":
        form = PerfilForm(request.POST,      instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request,'perfiles/editar_perfil.html', {'form':form})

def tutorial(request):
    if "login_status" in request.COOKIES and "username" in request.COOKIES:
        context = {
            'username': request.COOKIES["username"],
            'login_status': request.COOKIES.get("login_status")
        }
        return render(request, 'perfiles/perfil.html', context)
    else:
        return render(request,'perfiles/tutorial.html')

def tutorial_sesionIniciada(request):
    return render(request,'perfiles/tutorial_sesionIniciada.html')

# Create your views here.
