from random import randint
import os
import json

static_data_path = os.path.join(os.path.dirname(__file__), "../staticData")

with open(f"{static_data_path}/information/abilities.json") as class_file:
    abilities = json.load(class_file)


def ability_dice_roll():
    while True:
        ability_score = sorted([randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)])
        abil = ability_score[1] + ability_score[2] + ability_score[3]
        if abil > 3:
            return abil

def ability_score():
    return [ability_dice_roll(), ability_dice_roll(), ability_dice_roll(), ability_dice_roll(), ability_dice_roll(), ability_dice_roll()]


def subclasses_for_class(TEMP_CHAR, CLASSES, SUBCLASSES):
    if int(TEMP_CHAR["level"]) >= CLASSES[TEMP_CHAR["class"]]["chose_subclass_level"]:
        subclasses = [(subclass["subclass_id"], subclass["subclass_name"]) for subclass in SUBCLASSES if
                      subclass["class_id"] == CLASSES[TEMP_CHAR["class"]]["class_id"]]
        return subclasses


def subraces_for_race(TEMP_CHAR, RACE, SUBRACE):
    subraces = [(subrace["subrace_id"], subrace["subrace_name"]) for subrace in SUBRACE if
                subrace["race_id"] == RACE[TEMP_CHAR["race"]]["race_id"]]
    return subraces


def get_abilities(ability_dict):
    ability = {
        "num": ability_dict["number"],
        "options": [(option, abilities["abilities"][option]["translate"]) for option in ability_dict["options"]]
    }
    return ability


def get_languages(RACE, BACKGROUNDS, TEMP_CHAR):
    languages = {
        "num": 0,
        "options": []
    }
    known_languages = [lang for lang in RACE["languages"]]
    if BACKGROUNDS["backgrounds"][TEMP_CHAR["backgrounds"]]["else_bonus"]["name"] == "Languages":
        languages["num"] += BACKGROUNDS["backgrounds"][TEMP_CHAR["backgrounds"]]["else_bonus"]["val"]
    if RACE["additional_languages"]:
        languages["num"] += RACE["additional_languages"]

    for language in BACKGROUNDS["languages"]:
        if language in known_languages:
            pass
        else:
            languages["options"].append((language, BACKGROUNDS["languages"][language]["translate"]))
    return languages
