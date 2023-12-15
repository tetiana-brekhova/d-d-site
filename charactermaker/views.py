import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import MyForm
import os
import cgi

from random import randint

static_data_path = os.path.join(os.path.dirname(__file__), "../staticData")

TEMP_CHAR = {
    "name": "",
    "class": "",
    "race": "",
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


# def ability_score():
#     while True:
#         ability_score = sorted([randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)])
#         abil = ability_score[1] + ability_score[2] + ability_score[3]
#         if abil > 3:
#             return abil


def charactermaker(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            # TODO: create obj in models

            TEMP_CHAR["name"] = form.cleaned_data.get("chr_name")
            TEMP_CHAR["class"] = form.cleaned_data.get('chr_class')
            TEMP_CHAR["race"] = form.cleaned_data.get('chr_race')
            TEMP_CHAR["backgrounds"] = form.cleaned_data.get("backgrounds")
            TEMP_CHAR["alignment"] = form.cleaned_data.get("alignment")
            TEMP_CHAR["appearance"] = form.cleaned_data.get("appearance")
            TEMP_CHAR["biography"] = form.cleaned_data.get("biography")
            TEMP_CHAR["level"] = form.cleaned_data.get("chr_level")
        return redirect("charactermaker:page")
    else:
        form = MyForm()
    return render(request, 'usersguid/charactermaker.html', {"form": form})


def page(request):
    if request.method == 'POST':
        equip_keys = [request.POST.get("1"), request.POST.get("2"), request.POST.get("3")]

        print(equip_keys)
        return HttpResponse(request)
    # TODO: add func "select_features" in models

    equipment = CLASSES[TEMP_CHAR["class"]]["start_equipment"]
    subclasses = []
    class_ = CLASSES[TEMP_CHAR["class"]]
    ideals = []
    traits = []
    bonds = []
    flaws = []
    equip = []
    abil = []
    if int(TEMP_CHAR["level"]) >= CLASSES[TEMP_CHAR["class"]]["chose_subclass_level"]:
        for sub in SUBCLASSES:
            if sub["class_id"] == CLASSES[TEMP_CHAR["class"]]["class_id"]:
                subclasses.append(sub["subclass_name"])

    return render(request, 'usersguid/page.html', {"start_equipment": equipment,
                                                   "subclasses": subclasses, "class": class_})


def page2(request):
    return HttpResponse(request)

# {% url 'charactermaker:page' race.race_eng_name, subrace.subrace_eng_name%}
# {% url 'charactermaker:page' class.class_eng_name %}
