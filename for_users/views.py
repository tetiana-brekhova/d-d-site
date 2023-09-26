from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def usersguid(request):
    return render(request, 'usersguid/usersguid.html')

def charactermaker(request):
    return render(request, 'usersguid/charactermaker.html')

def races(request):
    return render(request, 'usersguid/races.html')

def classes(request):
    return render(request, 'usersguid/classes.html')

def personality(request):
    return render(request, 'usersguid/personality.html')

def equipment(request):
    return render(request, 'usersguid/equipment.html')

def magic(request):
    return render(request, 'usersguid/magic.html')