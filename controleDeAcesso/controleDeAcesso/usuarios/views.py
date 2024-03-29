from django.shortcuts import render, redirect
from django.conf import settings
from .models import UsuariosModel
from .models import HistoricoModel
from .forms import UsuariosForm
from .forms import HistoricoForm
import base64


def index(request):
    usuarios = UsuariosModel.objects.all()
    template_name = 'usuarios/index.html'
    context = {
        'usuarios': usuarios
    }
    return render(request, template_name, context)


def historico(request):
    historico = HistoricoModel.objects.all()
    template_name = 'usuarios/historico.html'
    context = {
        'historico': historico
    }
    return render(request, template_name, context)


def cadastro(request):
	usuario = UsuariosModel.objects.all()

	context = {}
	if request.method == 'POST':
		form = UsuariosForm(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			# print(form.cleaned_data['image_i'])
			img = base64.standard_b64encode(form.cleaned_data['image_i'].encode())
			print(form.cleaned_data['image_i'])
			print('====================')
			print(form.cleaned_data['image_i'].encode())
			print('====================')
			print(img)
			with open("/home/caio/imageToSave.jpeg", "wb") as fh:
				fh.write(base64.decodebytes(img))




			#print(form.cleaned_data['name']) #mostra os valores no prompt que foi enviado no campo
			form.save()
			form = UsuariosForm() #limpar o formulário após enviar os dados digitados nos campos
			return redirect('usuarios:index')
	else:
		form = UsuariosForm()
	context['form'] = form
	context['usuario'] = usuario
	template_name = 'usuarios/cadastro.html'
	return render(request, template_name, context)