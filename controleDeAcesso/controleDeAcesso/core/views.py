from django.shortcuts import render
from django.http import HttpResponse
import mimetypes

def home(request):
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')

def access_control(request):
    return render(request, 'access_control.html')


def users(request):
    return render(request, 'users.html')