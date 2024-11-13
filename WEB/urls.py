# nombre_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',LoginView.as_view(template_name='WEB/login.html'),name='login')
]

