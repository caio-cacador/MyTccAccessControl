from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import CadastroForm

@login_required
def painel(request):
	template_name = 'contas/painel.html'
	return render(request, template_name)

def cadastro(request):
	template_name = 'contas/cadastro.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username=user.username, password=form.cleaned_data['password1'])
			login(request, user)
			return redirect('core:home')
	else:
		form = UserCreationForm()
	context = {
		'form': form
	}
	return render(request, template_name, context)