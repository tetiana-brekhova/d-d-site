import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import os


CLASSES = {}
RACES = {}
SPELLS = {}

script_dir = os.path.dirname(__file__)
rel_path = "../staticData"
static_data_path = os.path.join(script_dir, rel_path)


for file in os.listdir(f"{static_data_path}/races")[::-1]:
    race_name = os.fsdecode(file)
    with open(f"{static_data_path}/races/{race_name}") as my_file:
        RACES[(file.split('-'))[0]] = json.load(my_file)

for file in os.listdir(f"{static_data_path}/classes"):
    class_name = os.fsdecode(file)
    with open(f"{static_data_path}/classes/{class_name}") as my_file:
        CLASSES[(file.split('-'))[0]] = json.load(my_file)

for file in os.listdir(f"{static_data_path}/spells/classSpell"):
    spell_class = os.fsdecode(file)
    with open(f"{static_data_path}/spells/classSpell/{spell_class}") as spell_file:
        SPELLS[(file.split('.'))[0]] = json.load(spell_file)


def usersguid(request):
    return render(request, 'usersguid/usersguid.html')

def charactermaker(request):
    return render(request, 'usersguid/charactermaker.html')

def races(request):
    context = RACES
    return render(request, 'usersguid/race/races.html', {"context": list(context.items()) })

def show_race(request, race):
    race = RACES[f"{race}"]
    return render(request, 'usersguid/race/race.html', {"context": race })


def classes(request):
    context = CLASSES
    return render(request, 'usersguid/class/classes.html', {"context": list(context.items()) })

def personality(request):
    return render(request, 'usersguid/information/personality.html')

def equipment(request):
    return render(request, 'usersguid/information/equipment.html')

def magic(request):
    with open(f"{static_data_path}/spells/spell_start_screen.json") as my_file:
        spell_data = json.load(my_file)
    section1 = spell_data["section1"]
    section2 = spell_data["section2"]
    return render(request, 'usersguid/spells/magic.html', {"section1": section1, "section2": section2, "classes": list(SPELLS.items())})

def languages(request):
    pass
