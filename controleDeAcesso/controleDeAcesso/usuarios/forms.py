from django import forms
from django.conf import settings
from .models import UsuariosModel, HistoricoModel

class UsuariosForm(forms.ModelForm):

	name = forms.CharField(label='Nome', max_length=100)

	class Meta:
		model = UsuariosModel
		fields = ['name']
	

class HistoricoForm(forms.ModelForm):

	usuario = UsuariosForm()

	class Meta:
		model = HistoricoModel
		fields = ['usuario']
	