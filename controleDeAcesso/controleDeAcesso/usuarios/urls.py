from django.urls import path
from controleDeAcesso.usuarios import views
app_name = 'usuarios' 

urlpatterns = [
   path("", views.index, name='index'),
   path("cadastro", views.cadastro, name='cadastro'), 
   path("historico", views.historico, name='historico'),        
]