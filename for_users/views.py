import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import os

static_data_path = os.path.join(os.path.dirname(__file__), "../staticData")

with open(f"{static_data_path}/races/races.json") as race_file:
    RACES = json.load(race_file)

with open(f"{static_data_path}/races/subraces.json") as race_file:
    SUBRACES = json.load(race_file)

with open(f"{static_data_path}/classes/classes.json") as class_file:
    CLASSES = json.load(class_file)


with open(f"{static_data_path}/classes/subclasses.json") as class_file:
    SUBCLASSES = json.load(class_file)

with open(f"{static_data_path}/spells/spells.json") as spell_file:
    SPELLS = json.load(spell_file)


def usersguid(request):
    return render(request, 'usersguid/usersguid.html')


def races(request):
    context = RACES
    return render(request, 'usersguid/race/races.html', {"context": context})


def show_race(request, race):
    for r in RACES:
        if r["race_eng_name"] == race:
            correct_race = r
    return render(request, 'usersguid/race/race.html', {"context": correct_race,
                                                        "subraces": SUBRACES})


def classes(request):
    context = CLASSES
    return render(request, 'usersguid/class/classes.html', {"context": context})


def show_class(request, classs):
    for c in CLASSES:
        if c["class_eng_name"] == classs:
            correct_class = c
    return render(request, 'usersguid/class/class.html', {"context": correct_class,
                                                          "subclasses": SUBCLASSES})


def personality(request):
    return render(request, 'usersguid/information/personality.html')


def equipment(request):
    return render(request, 'usersguid/information/equipment.html')


def magic(request):
    with open(f"{static_data_path}/spells/spell_start_screen.json") as my_file:
        spell_data = json.load(my_file)
    section1 = spell_data["section1"]
    section2 = spell_data["section2"]
    return render(request, 'usersguid/spells/magic.html',
                  {"section1": section1, "section2": section2})

def class_spells(request, class_id):
    cantrips = [spell for spell in SPELLS["cantrips"] if class_id in spell["class_id"]]
    first = [spell for spell in SPELLS["1"] if class_id in spell["class_id"]]


def languages(request):
    pass
