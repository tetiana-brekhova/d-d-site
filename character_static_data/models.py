from django.db import models


class Languages(models.Model):
    language_name = models.CharField(blank=True, max_length=50)

    @staticmethod
    def add_language(language_name):
        new_language = Languages()
        new_language.language_name = language_name
        new_language.save()
        return new_language

    @staticmethod
    def get_by_id(language_id):
        return Languages.objects.get(id=language_id) if Languages.objects.filter(id=language_id) else None

    @staticmethod
    def get_all():
        return list(Languages.objects.all())


class Skills(models.Model):
    skill_name = models.CharField(blank=True, max_length=50)
    skill_value = 0
    skill_modifier = (skill_value-10)//2


    class Meta:
        ordering = ["skill_name"]

    def __str__(self):
        return self.skill_name

    @staticmethod
    def add_skill(skill_name):
        new_skill = Skills()
        new_skill.skill_name = skill_name
        new_skill.save()
        return new_skill


    # def add_skill_val(self, value):
    #     self.skill_value = value


    @staticmethod
    def get_by_id(skill_id):
        return Skills.objects.get(id=skill_id) if Skills.objects.filter(id=skill_id) else None

    @staticmethod
    def get_all():
        return list(Skills.objects.all())


class Abilities(models.Model):
    ability_name = models.CharField(blank=True, max_length=100)
    ability_base = models.ManyToManyField(Skills)

    class Meta:
        ordering = ["ability_name"]

    def __str__(self):
        return self.ability_name

    @staticmethod
    def add_ability(ability_name, base_skill=None):
        new_ability = Abilities()
        new_ability.ability_name = ability_name
        new_ability.base_skill.add(base_skill)
        new_ability.save()
        return new_ability

    @staticmethod
    def get_by_id(ability_id):
        return Abilities.objects.get(id=ability_id) if Abilities.objects.filter(id=ability_id) else None


    @staticmethod
    def delete_by_id(ability_id):
        if Abilities.get_by_id(ability_id) is None:
            return False
        Abilities.objects.get(id=ability_id).delete()
        return True


    @staticmethod
    def get_all():
        return list(Abilities.objects.all())


class Feats(models.Model):
    feats_name = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=500)
    bonus_skill = models.ManyToManyField(Skills)
    bonus_value = models.IntegerField()


    class Meta:
        ordering = ["feats_name"]

    def __str__(self):
        return self.feats_name

    @staticmethod
    def add_feats(feats_name, description, bonus_skill, bonus_value):
        new_feats = Feats()
        new_feats.feats_name = feats_name
        new_feats.description = description
        new_feats.bonus_skill = bonus_skill
        new_feats.bonus_value = bonus_value
        new_feats.save()
        return new_feats

    @staticmethod
    def get_by_id(feats_id):
        return Feats.objects.get(id=feats_id) if Feats.objects.filter(id=feats_id) else None

    @staticmethod
    def get_all():
        return list(Feats.objects.all())
