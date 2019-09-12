from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from controleDeAcesso.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastrar-se/', views.register, name='register'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar-conta/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
    path('nova-senha/', views.password_reset, name='password_reset'),

    path("confirmar-nova-senha/<key>/", views.password_reset_confirm, name='password_reset_confirm')
]
