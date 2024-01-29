import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import MyForm
from .models import Character
import os
import cgi
from .help_func import *

static_data_path = os.path.join(os.path.dirname(__file__), "../staticData")

# TODO: add else fields

TEMP_CHAR = {
    "name": "",
    "class": "",
    "race": "",
    "sex": "",
    "backgrounds": "",
    "alignment": "",
    "appearance": "",
    "biography": "",
    "level": ""
}

with open(f"{static_data_path}/races/races.json") as race_file:
    RACES = json.load(race_file)

with open(f"{static_data_path}/races/subraces.json") as race_file:
    SUBRACES = json.load(race_file)

with open(f"{static_data_path}/classes/classes.json") as class_file:
    CLASSES = json.load(class_file)

with open(f"{static_data_path}/classes/subclasses.json") as class_file:
    SUBCLASSES = json.load(class_file)

with open(f"{static_data_path}/information/character_pesonality.json") as class_file:
    BACKGROUNDS = json.load(class_file)


def charactermaker(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            TEMP_CHAR["name"] = form.cleaned_data.get("chr_name")
            TEMP_CHAR["class"] = form.cleaned_data.get('chr_class')
            TEMP_CHAR["race"] = form.cleaned_data.get('chr_race')
            TEMP_CHAR["sex"] = form.cleaned_data.get('sex')
            TEMP_CHAR["backgrounds"] = form.cleaned_data.get("backgrounds")
            TEMP_CHAR["alignment"] = form.cleaned_data.get("alignment")
            TEMP_CHAR["appearance"] = form.cleaned_data.get("appearance")
            TEMP_CHAR["biography"] = form.cleaned_data.get("biography")
            TEMP_CHAR["level"] = form.cleaned_data.get("chr_level")
        return redirect("charactermaker:page")
    else:
        form = MyForm()
        abil_dice = ability_score()
    return render(request, 'usersguid/charactermaker.html', {"form": form, "dice": abil_dice})


def page(request):
    if request.method == 'POST':
        # equip_keys = [request.POST.get("subclass")]
        # print(request.POST.getlist("ability"))
        return HttpResponse(request)
    subraces = subraces_for_race(TEMP_CHAR, RACES, SUBRACES)
    equipment = CLASSES[TEMP_CHAR["class"]]["start_equipment"]
    subclasses = subclasses_for_class(TEMP_CHAR, CLASSES, SUBCLASSES)
    personality = BACKGROUNDS["backgrounds"][TEMP_CHAR["backgrounds"]]
    ability = get_abilities(CLASSES[TEMP_CHAR["class"]]["proficiencies"][3])
    languages = get_languages(RACES[TEMP_CHAR["race"]], BACKGROUNDS, TEMP_CHAR)
    return render(request, 'usersguid/page.html', {"start_equipment": equipment,
                                                   "subclasses": subclasses, "ability": ability,
                                                   "personality": personality, "subraces": subraces,
                                                   "languages": languages})


def agree_page():
    pass

# {% url 'charactermaker:page' race.race_eng_name, subrace.subrace_eng_name%}
# {% url 'charactermaker:page' class.class_eng_name %}
