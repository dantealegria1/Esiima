from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio (login)
    path('login/', views.login_view, name='login'),  # Vista para manejar el login
    path('secciones/', views.secciones_view, name='secciones'),  # Página a la que se redirige después de iniciar sesión
]

