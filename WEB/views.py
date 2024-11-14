from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Vista de inicio (home)
def home(request):
    return render(request, 'WEB/login.html')

# Vista para manejar el login
def login_view(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        username = request.POST.get('usuario')
        password = request.POST.get('password')
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Iniciar sesión al usuario
            login(request, user)
            
            # Redirigir a la página 'secciones.html'
            return redirect('secciones')  # Redirige a secciones
            
        else:
            # Si la autenticación falla, mostrar un mensaje de error
            return HttpResponse("Usuario o contraseña incorrectos")
    
    # Si es un GET, mostrar el formulario
    return render(request, 'WEB/login.html')

# Vista para la página 'secciones'
def secciones_view(request):
    return render(request, 'WEB/secciones.html')
