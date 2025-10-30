from django.shortcuts import render,redirect
from .models import Perfil
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm

@login_required
def ver_perfil(request):
    perfil = request.user.perfil
    return render(request, 'perfiles/ver_perfil.html', {'perfil':perfil})

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
    return render(request,'perfiles/tutorial.html')


# Create your views here.
