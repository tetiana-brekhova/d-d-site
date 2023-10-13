from django.db import models


class Race(models.Model):
    race_name = models.CharField(blank=True, max_length=100)
    img_path = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=1000)
    full_description = models.JSONField(blank=True)
    race_bonus = models.JSONField(blank=True)
    max_age = models.IntegerField(blank=True)
    size = models.CharField(blank=True, max_length=50)
    speed = models.IntegerField(blank=True)
    languages = models.CharField(blank=True, max_length=128)
    else_traits = models.CharField(blank=True, max_length=128)

    # def __str__(self):
    #     return f"race_name: {self.race_name}, " \
    #            f"img_path: {self.img_path}," \
    #            f" description: {self.description}," \
    #            f" race_bonus: {self.race_bonus}," \
    #            f" max_age: {self.max_age}," \
    #            f" size: {self.size}," \
    #            f" speed: {self.speed}," \
    #            f" languages: {self.languages}," \
    #            f" else_traits: {self.else_traits},"

    @staticmethod
    def create_new_race(name: str, img_path: str, max_age: int, size: int, speed: int,
                        languages: str, else_traits: str, description: str, full_description: dict, race_bonus: dict):

        new_race = Race()
        new_race.race_name = name
        new_race.img_path = img_path
        new_race.max_age = max_age
        new_race.size = size
        new_race.speed = speed
        new_race.languages = languages
        new_race.else_traits = else_traits
        new_race.description = description
        new_race.full_description = full_description
        new_race.race_bonus = race_bonus
        new_race.save()
        return new_race

    @staticmethod
    def get_by_id(race_id):
        return Race.objects.get(id=race_id) if Race.objects.filter(id=race_id) else None

    @staticmethod
    def delete_by_id(race_id):
        if Race.get_by_id(race_id) is None:
            return False
        Race.objects.get(id=race_id).delete()
        return True

    @staticmethod
    def get_all():
        return list(Race.objects.all())

    def add_changes(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()


class CharacterClass(models.Model):
    class_name = models.CharField(blank=True, max_length=100)
    subclass = models.CharField(blank=True, max_length=100)
    class_level = 0
    poficiency_bonus = 0
    base_spell_attack_modifier = 0
    base_ability = models.CharField(blank=True, max_length=100)
    img_path = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=1000)
    full_description = models.JSONField(blank=True)
    advice = models.CharField(blank=True, max_length=1000)
    hit_dice = models.IntegerField(blank=True)
    proficiencies = models.JSONField(blank=True)
    ability = models.JSONField(blank=True)
    # {"Armor": "", "Weapons": "", "Tools": "", "Saving Throws": "", "Skills": ""}
    class_equipment = models.JSONField(blank=True)
    base_spell_save_dc = models.IntegerField(blank=True)
    spells = models.JSONField(blank=True)
    # {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[],
    #           13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[]}
    skills = models.JSONField(blank=True)
    # {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[],
    #           13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[]}
    spell_slot = models.JSONField(blank=True)

    # {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    @staticmethod
    def create_new_class(class_name: str, subclass: str,
                         img_path: str, description: str, full_description: dict, advice: str,
                         hit_dice: int, proficiencies: dict, ability: dict, class_equipment: dict,
                         base_spell_save_dc: int, spells: dict,
                         skills: dict, spell_slot: dict):

        new_class = CharacterClass()

        new_class.class_name = class_name
        new_class.subclass = subclass
        new_class.img_path = img_path
        new_class.description = description
        new_class.full_description = full_description
        new_class.advice = advice
        new_class.hit_dice = hit_dice
        new_class.proficiencies = proficiencies
        new_class.ability = ability
        new_class.class_equipment = class_equipment
        new_class.base_spell_save_dc = base_spell_save_dc
        new_class.spells = spells
        new_class.skills = skills
        new_class.spell_slot = spell_slot

        new_class.save()
        return new_class

    @staticmethod
    def get_by_id(class_id):
        return CharacterClass.objects.get(id=class_id) if CharacterClass.objects.filter(id=class_id) else None

    @staticmethod
    def delete_by_id(class_id):
        if CharacterClass.get_by_id(class_id) is None:
            return False
        CharacterClass.objects.get(id=class_id).delete()
        return True

    @staticmethod
    def get_all():
        return list(CharacterClass.objects.all())

    def add_changes(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

# class Character:
#
#     def __init__(self, name, age, class_name, race_name):
#         name = name
#         class_ = race_name
#         race = class_name
#         age = age
#         ability = {"Strength":0, "Dexterity":0, "Constitution":0, "Intelligence":0, "Wisdom":0, "Charisma":0}
#
#     def create_class(self):
#         return Class_(class_name=self.class_)
#
#     def create_race(self):
#         return Race(race_name=self.race)

