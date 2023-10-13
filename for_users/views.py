import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import os


def usersguid(request):
    return render(request, 'usersguid/usersguid.html')

def charactermaker(request):
    return render(request, 'usersguid/charactermaker.html')

def races(request):
    races_list = {}
    for file in os.listdir("/var/www/test_project/app/for_users/staticData/races"):
        race_name = os.fsdecode(file)
        with open(f"/var/www/test_project/app/for_users/staticData/races/{race_name}") as my_file:
            races_list[(file.split('-'))[0]] = json.load(my_file)
    context = races_list
    return render(request, 'usersguid/races.html', {"context": list(context.items()) })

def classes(request):
    class_list = {}
    for file in os.listdir("/var/www/test_project/app/for_users/staticData/classes"):
        class_name = os.fsdecode(file)
        with open(f"/var/www/test_project/app/for_users/staticData/classes/{class_name}") as my_file:
            class_list[(file.split('-'))[0]] = json.load(my_file)
    context = class_list
    return render(request, 'usersguid/classes.html', {"context": list(context.items()) })

def personality(request):
    return render(request, 'usersguid/personality.html')

def equipment(request):
    return render(request, 'usersguid/equipment.html')

def magic(request):
    with open(f"/var/www/test_project/app/for_users/staticData/spells/spell_start_screen.json") as my_file:
        class_list = json.load(my_file)
    section1 = class_list["data"][0]["section1"]
    section2 = class_list["data"][0]["section2"]
    return render(request, 'usersguid/magic.html', {"section1": section1, "section2": section2})

def languages(request):
    pass


