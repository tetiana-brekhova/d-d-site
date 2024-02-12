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


with open(f"{static_data_path}/classes/subclasses.json") as subclass_file:
    SUBCLASSES = json.load(subclass_file)

with open(f"{static_data_path}/spells/spells.json") as spell_file:
    SPELLS = json.load(spell_file)


def usersguid(request):
    return render(request, 'usersguid/usersguid.html')


def races(request):
    context = [RACES[r] for r in RACES]
    return render(request, 'usersguid/race/races.html', {"context": context})


def show_race(request, race):
    for r in RACES:
        if RACES[r]["race_eng_name"] == race:
            correct_race = RACES[r]
    return render(request, 'usersguid/race/race.html', {"context": correct_race,
                                                        "subraces": SUBRACES})


def classes(request):
    context = [CLASSES[c] for c in CLASSES]
    return render(request, 'usersguid/class/classes.html', {"context": context})


def show_class(request, classs):
    for c in CLASSES:
        if CLASSES[c]["class_eng_name"] == classs:
            correct_class = CLASSES[c]
    subclasses = [SUBCLASSES[subclass] for subclass in SUBCLASSES if SUBCLASSES[subclass]["class_id"] == correct_class["class_id"]]
    return render(request, 'usersguid/class/class.html', {"context": correct_class,
                                                          "subclasses": subclasses})


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
    # add last spell 3 page
    if class_id == "0":
        cantrips = [SPELLS["cantrips"][spell] for spell in SPELLS["cantrips"]]
        first = [SPELLS["1st"][spell] for spell in SPELLS["1st"]]
        class_name = "всіх клас"
        return render(request, 'usersguid/spells/class_spells.html',
                      {"name": class_name, "cantrips": cantrips, "first": first})
    else:
        cantrips = [SPELLS["cantrips"][spell] for spell in SPELLS["cantrips"] if int(class_id) in SPELLS["cantrips"][spell]["class_id"]]
        first = [SPELLS["1st"][spell] for spell in SPELLS["1st"] if int(class_id) in SPELLS["1st"][spell]["class_id"]]
        class_name = ""
        for c in CLASSES:
            if CLASSES[c]["class_id"] == int(class_id):
                class_name = CLASSES[c]["class_name"]
        return render(request, 'usersguid/spells/class_spells.html',
                      {"name": class_name, "cantrips": cantrips, "first": first})



def languages(request):
    pass
