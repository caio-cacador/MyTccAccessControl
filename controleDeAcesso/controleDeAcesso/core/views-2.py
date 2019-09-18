from django.utils import translation
from django.shortcuts import render
from django.http import HttpResponse
import subprocess


import logging
logger = logging.getLogger(__name__)

def home(request):
    translation.activate('en')
    return render(request, 'home.html', {'usuario': 'Caio Cacador'})


def contact(request):
    translation.activate('en')
    return render(request, 'contact.html')


def access_control(request):
    translation.activate('en')
    return render(request, 'access_control.html')


def users(request):
    translation.activate('en')
    return render(request, 'users.html')
    