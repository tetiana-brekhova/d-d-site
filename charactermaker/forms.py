from django import forms
import os
import json


static_data_path = os.path.join(os.path.dirname(__file__), "../staticData")

with open(f"{static_data_path}/races/races.json") as race_file:
    RACES = json.load(race_file)

with open(f"{static_data_path}/races/subraces.json") as race_file:
    SUBRACES = json.load(race_file)

with open(f"{static_data_path}/classes/classes.json") as class_file:
    CLASSES = json.load(class_file)



class MyForm(forms.Form):
    CHR_RACE = []
    for race in RACES:
        if race["subraces"]:
            for subrace in SUBRACES:
                if race["race_id"] == subrace["race_id"]:
                    CHR_RACE.append((subrace["subrace_eng_name"], subrace["subrace_name"]))
        else:
            CHR_RACE.append((race["race_eng_name"], race["race_name"]))
    chr_race = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHR_RACE,
    )
    CHR_CLASS = [(c["class_eng_name"], c["class_name"]) for c in CLASSES]
    chr_class = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHR_CLASS,
    )


