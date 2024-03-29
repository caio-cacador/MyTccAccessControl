from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from controleDeAcesso.core.mail import send_mail_template
from controleDeAcesso.core.utils import generate_hash_key

from .models import PasswordReset


User = get_user_model()


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            'Nenhum usuário encontrado com este e-mail'
        )

    def save(self):
        template_name = 'password_reset_email.html'
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        subject = 'Criar nova senha de Controle de Acesso'
        context = {'reset': reset}
        send_mail_template(subject, template_name, context,[user.email])


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não são iguais.')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     queryset = User.objects.filter(
    #         email=email).exclude(pk=self.instance.pk
    #     )
    #     if queryset.exists():
    #         raise forms.ValidationError('E-mail já em uso.')
    #     return email

    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name', 'last_name']
        fields = ['username', 'email', 'name']
