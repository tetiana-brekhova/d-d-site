import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import MyForm
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

def charactermaker(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            races = form.cleaned_data.getlist('chr_race')
            char_class = form.cleaned_data.getlist('chr_class')
            print(races, char_class)
    else:
        form = MyForm()
    return render(request, 'usersguid/charactermaker.html', {"form": form})

    #     char_class = request.GET.get("class", "")
    #     char_race = request.GET.get("races", "")
    #     print(f"{char_class}, {char_race}, 15")
    #
    # return render(request, 'usersguid/charactermaker.html', {"races": RACES,
    #                                                          "classes": CLASSES,
    #                                                          "subclasses": SUBCLASSES,
    #                                                          "subraces": SUBRACES})



def page(request):

    # return render(request, 'usersguid.html', {'form': form})
    return HttpResponse(request)


# {% url 'charactermaker:page' race.race_eng_name, subrace.subrace_eng_name%}
# {% url 'charactermaker:page' class.class_eng_name %}
