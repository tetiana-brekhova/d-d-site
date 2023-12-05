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
    CHR_RACE = []
    for race in RACES:
        if race["subraces"]:
            for subrace in SUBRACES:
                if race["race_id"] == subrace["race_id"]:
                    CHR_RACE.append((subrace["subrace_eng_name"], subrace["subrace_name"]))
        else:
            CHR_RACE.append((race["race_eng_name"], race["race_name"]))
    chr_race = forms.ChoiceField(
        widget=forms.Select,
        choices=CHR_RACE, label="Раса"
    )
    CHR_CLASS = [(c["class_eng_name"], c["class_name"]) for c in CLASSES]
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
        choices=[(s["eng_name"], s["name"]) for s in BACKGROUNDS["backgrounds"]],
        label="Передісторія"
    )
    chr_name = forms.CharField(widget=forms.Textarea, label="Ім'я")
    alignment = forms.ChoiceField(widget=forms.Select,
                                  choices=[("Законно-добрий", "Законно-добрий"),
                                           ("Законно-нейтральний", "Законно-нейтральний"),
                                           ("Законно-злий", "Законно-злий"), ("Нейтрально-добрий", "Нейтрально-добрий"),
                                           ("Нейтральний", "Нейтральний"), ("Нейтрально-злий", "Нейтрально-злий"),
                                           ("Хаотично-добрий", "Хаотично-добрий"),
                                           ("Хаотично-нейтральний", "Хаотично-нейтральний"),
                                           ("Хаотично-злий", "Хаотично-злий")],
                                  label="Світогляд"
                                  )
    appearance = forms.CharField(widget=forms.Textarea, label="Зовнішність")
    biography = forms.CharField(widget=forms.Textarea, label="Біографія")


