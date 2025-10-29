from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from .forms import RegistroForm
from perfiles.models import Perfil
def index(request):
    return render(request, 'registro_login/index.html', {})

def login_usuario(request):
    if request.method == "POST":
        nombre = request.POST['username']
        contraseña = request.POST['password']
        usuario = authenticate(request, username = nombre, password = contraseña)
        if usuario is not None:
            login(request,usuario)
            return redirect('ver_perfil')
        else:
            return redirect('login')
    else:
        return render(request, 'registro_login/login.html',{})
    
    
def logout_usuario(request):
    logout(request)
    return redirect('index')

def inicio(request):
    return render(request, 'registro_login/inicio.html', {})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = form.cleaned_data['username']
            contraseña = form.cleaned_data['password1']
            usuario = authenticate(request, username = nombre, password = contraseña)
            Perfil.objects.create(user = usuario, nombre = '')
            if usuario :
                login(request,usuario)
                messages.success(request, "Se ha registrado correctamente")
                return redirect('inicio')
            else:
                messages.error(request, "Inicio de sesión fallido, por favor inicie sesión nuevamente")
                return redirect('login')
    else:
        form = RegistroForm
    return render(request, 'registro_login/registro.html',{'form':form})

        
    # Create your views here.
