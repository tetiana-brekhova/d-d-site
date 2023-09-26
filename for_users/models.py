from django.db import models

class Race:

    def __init__(self, race_name):
        race_name = race_name
        img_path = ""
        description = ""
        race_bonus = {"Strength":0, "Dexterity":0, "Constitution":0, "Intelligence":0, "Wisdom":0, "Charisma":0}
        race_peculiarities = {}



class Class_:

    def __init__(self, class_name):
        class_name = class_name
        img_path = ""
        description = ""
        hit_dice = 0
        proficiencies = {"Armor": "", "Weapons": "", "Tools": "", "Saving Throws": "", "Skills": ""}
        class_equipment = []
        spell_save_DC = 0
        spell_attack_modifier = 0
        skills = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[],}
        spell_slot = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}


class Character:

    def __init__(self, name, age, class_name, race_name):
        name = name
        class_ = Class_(class_name)
        race = Race(race_name)
        age = age
        ability = {"Strength":0, "Dexterity":0, "Constitution":0, "Intelligence":0, "Wisdom":0, "Charisma":0}



