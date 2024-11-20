from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio (login)
    path('login/', views.login_view, name='login'),  # Vista para manejar el login
    path('secciones/', views.secciones_view, name='secciones'),  # Página de secciones
    path('cajas/', views.cajas_view, name='cajas'),  # Página de cajas
    path('situacion/', views.situacion_view, name='situacion'),  # Nueva sección
    path('materias/', views.materias_view, name='materias'),  # Otra sección
]
