from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def home(request):
    return render(request, 'WEB/login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('secciones')
        else:
            return HttpResponse("Usuario o contraseña incorrectos")
    return render(request, 'WEB/login.html')

def secciones_view(request):
    return render(request, 'WEB/secciones.html')

def cajas_view(request):
    return render(request, 'WEB/cajas.html')

def situacion_view(request):
    return render(request, 'WEB/situacion.html')

def materias_view(request):
    return render(request, 'WEB/materias.html')

