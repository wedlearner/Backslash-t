from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from .forms import RegistroForm
from perfiles.models import Perfil
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'registro_login/index.html')

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('perfiles:ver_perfil')
    else:
        if request.method == "POST":
            nombre = request.POST['username']
            contraseña = request.POST['password']
            usuario = authenticate(request, username = nombre, password = contraseña)

            if usuario is not None:
                login(request,usuario)
                return redirect('perfiles:ver_perfil')
            else:
                return redirect('registro_login:login')
        else:
            return render(request, 'registro_login/inicio_sesion.html',{})
    
    
def logout_usuario(request):
    logout(request)
    return redirect('registro_login:index')

def inicio(request):
    return render(request, 'registro_login/inicio.html', {})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            usuario = form.save()
            nombre = form.cleaned_data['username']
            contraseña = form.cleaned_data['password1']
            usuario = authenticate(request, username = nombre, password = contraseña)
            Perfil.objects.create(user = usuario, nombre = '')
            if usuario is not None:
                login(request,usuario)
                messages.success(request, "Se ha registrado correctamente")
                return redirect('perfiles:ver_perfil')
            else:
                messages.error(request, "Inicio de sesión fallido, por favor inicie sesión nuevamente")
                return redirect('registro_login:login')
        else:
            print(form.errors)
    else:
        if request.user.is_authenticated:
            return redirect('perfiles:ver_perfil')
        form = RegistroForm()
    return render(request, 'registro_login/inicio_sesion.html',{'form':form})

        
    # Create your views here.
