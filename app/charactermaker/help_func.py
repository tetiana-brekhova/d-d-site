from random import randint
import os
import json

static_data_path = os.path.join(os.path.dirname(__file__), "../staticData")

with open(f"{static_data_path}/information/abilities.json") as class_file:
    abilities = json.load(class_file)


def ability_score(num, dise):
    while True:
        ability_score = sorted([randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)])
        abil = ability_score[1] + ability_score[2] + ability_score[3]
        if abil > 3:
            return abil


def subclasses_for_class(TEMP_CHAR, CLASSES, SUBCLASSES):
    if int(TEMP_CHAR["level"]) >= CLASSES[TEMP_CHAR["class"]]["chose_subclass_level"]:
        subclasses = [(subclass["subclass_id"], subclass["subclass_name"]) for subclass in SUBCLASSES if
                      subclass["class_id"] == CLASSES[TEMP_CHAR["class"]]["class_id"]]
        return subclasses


def get_abilities(ability_dict):
    ability = {
        "num": ability_dict["number"],
        "options": [(option, abilities["abilities"][option]["translate"]) for option in ability_dict["options"]]
    }
    return ability
