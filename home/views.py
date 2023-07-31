from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# from .forms import LoginForm, RegisterForm

def homepage(request):
    # return HttpResponse("Test")
    if request.method == 'GET':
        return render(request, 'home.html')
