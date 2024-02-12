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

START_ABILITIES_VALUE = {
    "Strength": "",
    "Dexterity": "",
    "Constitution": "",
    "Intelligence": "",
    "Wisdom": "",
    "Charisma": ""
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

with open(f"{static_data_path}/spells/spells.json") as spell_file:
    SPELLS = json.load(spell_file)


def charactermaker(request):
    form = MyForm(request.POST)
    if request.method == 'POST':
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
            START_ABILITIES_VALUE["Strength"] = form.cleaned_data.get("strength")
            START_ABILITIES_VALUE["Dexterity"] = form.cleaned_data.get("dexterity")
            START_ABILITIES_VALUE["Constitution"] = form.cleaned_data.get("constitution")
            START_ABILITIES_VALUE["Intelligence"] = form.cleaned_data.get("intelligence")
            START_ABILITIES_VALUE["Wisdom"] = form.cleaned_data.get("wisdom")
            START_ABILITIES_VALUE["Charisma"] = form.cleaned_data.get("charisma")
        return redirect("charactermaker:personality_creation")
    else:
        abil_dice = ability_score()
    return render(request, 'usersguid/charactermaker.html', {"form": form, "dice": abil_dice})


def personality_creation(request):
    subraces = subraces_for_race(TEMP_CHAR, RACES, SUBRACES)
    equipment = CLASSES[TEMP_CHAR["class"]]["start_equipment"]
    subclasses = subclasses_for_class(TEMP_CHAR, CLASSES, SUBCLASSES)
    personality = BACKGROUNDS["backgrounds"][TEMP_CHAR["backgrounds"]]
    ability = get_abilities(CLASSES[TEMP_CHAR["class"]]["proficiencies"][3])
    languages = get_languages(RACES[TEMP_CHAR["race"]], BACKGROUNDS, TEMP_CHAR)
    if request.method == 'POST':
        subclass = request.POST.get("subclass")
        if CLASSES[TEMP_CHAR["class"]]["spellcasting"]:
            return redirect("charactermaker:spells_chooser")
        elif subclass and SUBRACES[subclass]["spellcasting"] and TEMP_CHAR["level"] > SUBRACES[subclass]["spellcasting_level"]:
            return redirect("charactermaker:spells_chooser")
        else:
            return redirect("charactermaker:confirm_character")
    return render(request, 'usersguid/personality_creation.html', {"start_equipment": equipment,
                                                   "subclasses": subclasses, "ability": ability,
                                                   "personality": personality, "subraces": subraces,
                                                   "languages": languages})


def spells_chooser(request):
    known_spells = 0
    known_cantrips = CLASSES[TEMP_CHAR["class"]]["spell_slots"]["level_"+TEMP_CHAR["level"]]["cantrips_known"]
    spells_options = {}
    if TEMP_CHAR["class"] == "artificer":
        k_spells = (START_ABILITIES_VALUE["Intelligence"] - 10)//2 + int(TEMP_CHAR["level"])//2
        if k_spells < 1:
            known_spells += 1
        else:
            known_spells += k_spells
    else:
        known_spells += CLASSES[TEMP_CHAR["class"]]["spell_slots"]["level_"+TEMP_CHAR["level"]]["spells_known"]
    #TODO: add num of subclass known spells
    the_bigger_level_spell = list(CLASSES[TEMP_CHAR["class"]]["spell_slots"]["level_"+TEMP_CHAR["level"]])[-1]
    for level in SPELLS:
        # TODO: add spell id

        spells_options[level] = [spell for spell in SPELLS[level] if int(CLASSES[TEMP_CHAR["class"]]["class_id"]) in spell["class_id"]]
        if level == the_bigger_level_spell:
            break
    if request.method == 'POST':
        pass
    print(spells_options)
    return render(request, 'usersguid/spells_chooser.html')


def confirm_character(request):
    return render(request, 'usersguid/confirm_character.html')

# {% url 'charactermaker:page' race.race_eng_name, subrace.subrace_eng_name%}
# {% url 'charactermaker:page' class.class_eng_name %}
