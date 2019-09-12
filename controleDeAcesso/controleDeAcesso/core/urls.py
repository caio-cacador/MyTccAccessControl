from django.contrib import admin
from django.urls import path
from controleDeAcesso.core import views
app_name = 'core' 

urlpatterns = [
    path("", views.home, name="home"),
    path("contato/", views.contact, name="contact"),
    path('controle-de-acesso/', views.access_control, name='access_control'),
]