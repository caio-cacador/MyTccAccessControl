from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.utils import translation

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset


User = get_user_model()


@login_required
def dashboard(request):
    translation.activate('en')
    template_name = 'dashboard.html'
    return render(request, template_name)


@login_required
def logout(request):
    translation.activate('en')
    template_name = 'logout.html'
    return render(request, template_name)


def register(request):
    translation.activate('en')
    template_name = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, template_name, context)


@login_required
def edit(request):
    translation.activate('en')
    template_name = 'edit.html'
    context = {}
    print('cu')
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def edit_password(request):
    translation.activate('en')
    template_name = 'edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, template_name, context)


def password_reset(request):
    translation.activate('en')
    template_name = 'password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)

    if form.is_valid():
        form.save()
        context['sucess'] = True

    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    translation.activate('en')
    template_name = 'password_reset_confirm.html'
    context = {}

    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)

    if form.is_valid():
        form.save()
        context['sucess'] = True
    
    context['form'] = form
    return render (request, template_name, context) 