from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import os


def usersguid(request):
    return render(request, 'usersguid/usersguid.html')

def charactermaker(request):
    return render(request, 'usersguid/charactermaker.html')

def races(request):
    race_list = []
    # directory = os.fsencode("staticData/races")
    for file in os.listdir("/var/www/test_project/app/for_users/staticData/races"):
        class_name = os.fsdecode(file)
        with open(f"/var/www/test_project/app/for_users/staticData/races/{class_name}") as my_file:
            race_list.append(my_file.read())
    context = dict(enumerate(race_list))
    return render(request, 'usersguid/races.html', context=context)

def classes(request):
    return render(request, 'usersguid/classes.html')

def personality(request):
    return render(request, 'usersguid/personality.html')

def equipment(request):
    return render(request, 'usersguid/equipment.html')

def magic(request):
    return render(request, 'usersguid/magic.html')

