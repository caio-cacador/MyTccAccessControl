from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

class CadastroForm(UserCreationForm):
	#admin = forms.BooleanField(label='admin')

	def save(self, commit=True):
		user = super(CadastroForm, self).save(commit=False)
		user.admin = self.cleaned_data['admin']
		if commit:
			user.save()
		return user

