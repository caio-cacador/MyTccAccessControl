from django import forms
from django.conf import settings
from .models import UsuariosModel, HistoricoModel


class UsuariosForm(forms.ModelForm):
	name = forms.CharField(label='Nome', max_length=100)
	image_i = forms.CharField(widget=forms.Textarea, required=False)
	image_ii = forms.CharField(widget=forms.Textarea, required=False)
	image_iii = forms.CharField(widget=forms.Textarea, required=False)
	image_iv = forms.CharField(widget=forms.Textarea, required=False)
	image_v = forms.CharField(widget=forms.Textarea, required=False)
	image_vi = forms.CharField(widget=forms.Textarea, required=False)

	class Meta:
		model = UsuariosModel
		fields = ['name']
	

class HistoricoForm(forms.ModelForm):

	usuario = UsuariosForm()

	class Meta:
		model = HistoricoModel
		fields = ['usuario']
	