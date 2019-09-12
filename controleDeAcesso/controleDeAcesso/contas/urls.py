from django.urls import path
from controleDeAcesso.contas import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import logout_then_login
app_name = 'contas' 

urlpatterns = [
    path("", views.painel, name='painel'),
    path('entrar/', LoginView.as_view(template_name='contas/login.html') , name='login' ),
    path("cadastre-se", views.cadastro, name='cadastro'),
    path('sair/', logout_then_login,{'login_url': 'contas:login'} , name='logout' ),
]