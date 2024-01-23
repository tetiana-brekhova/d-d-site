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

with open(f"{static_data_path}/information/character_pesonality.json") as class_file:
    BACKGROUNDS = json.load(class_file)


class MyForm(forms.Form):
    CHR_RACE = [(RACES[r]["race_id"], RACES[r]["race_name"]) for r in RACES]
    chr_race = forms.ChoiceField(
        widget=forms.Select,
        choices=CHR_RACE, label="Раса"
    )
    CHR_CLASS = [(c, CLASSES[c]["class_name"]) for c in CLASSES]
    chr_class = forms.ChoiceField(
        widget=forms.Select,
        choices=CHR_CLASS, label="Клас"
    )
    LEVELS = [(n, n) for n in range(1, 21)]
    chr_level = forms.ChoiceField(widget=forms.Select,
                                  choices=LEVELS,
                                  label="Рівень"
                                  )
    backgrounds = forms.ChoiceField(
        widget=forms.Select,
        choices=[(BACKGROUNDS["backgrounds"][v]["eng_name"], BACKGROUNDS["backgrounds"][v]["name"]) for v in BACKGROUNDS["backgrounds"]],
        label="Передісторія"
    )
    chr_name = forms.CharField(widget=forms.Textarea, label="Ім'я")
    alignment = forms.ChoiceField(widget=forms.Select,
                                  choices=[(BACKGROUNDS["alignments"][v], BACKGROUNDS["alignments"][v]["name"]) for v in BACKGROUNDS["alignments"]],
                                  label="Світогляд"
                                  )
    sex = forms.ChoiceField(widget=forms.Select,
                                  choices=[("woman", "жіноча"), ("man", "чоловіча")],
                                  label="Стать"
                                  )
    appearance = forms.CharField(widget=forms.Textarea, label="Зовнішність")
    biography = forms.CharField(widget=forms.Textarea, label="Біографія")



