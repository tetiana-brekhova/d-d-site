from django.db import models


class Character(models.Model):
    name = models.CharField(blank=True, max_length=128)
    classs = models.CharField(blank=True, max_length=100)
    race = models.CharField(blank=True, max_length=100)
    sex = models.CharField(blank=True, max_length=128)
    backgrounds = models.CharField(blank=True, max_length=10000)
    alignment = models.CharField(blank=True, max_length=10000)
    appearance = models.CharField(blank=True, max_length=10000)
    biography = models.CharField(blank=True, max_length=10000)
    level = models.IntegerField()

    # age = models.IntegerField(blank=True)

    subrsce = models.CharField(blank=True, max_length=100)
    subclass = models.CharField(blank=True, max_length=100)
    start_characteristics = {}
    bonus_characteristics = {}
    languages = []
    size = ""
    equipment = ""
    skills = ""
    armor_class = ""
    max_hit_points = ""
    speed = ""
    abilities = {}
    money = {}

    user = ""


# class Meta:
#     ordering = ('name',)


def __str__(self):
    return f"'post_id': {self.post_id}, " \
           f"'post_name': '{self.post_name}', " \
           f"'post_body': '{self.post_body}', " \
           f"'post_data': {self.post_data}, " \
           f"'post_image': {self.post_image}, "
    # f"'authors': {[author.id for author in self.authors.all()]}" \


def __repr__(self):
    return f"Post(id={self.id})"


@staticmethod
def get_by_id(character_id):
    return Character.objects.get(id=character_id) if Character.objects.filter(id=character_id) else None


@staticmethod
def delete_by_id(character_id):
    if Character.get_by_id(character_id) is None:
        return False
    Character.objects.get(id=character_id).delete()
    return True


@staticmethod
def create(name, classs, race, sex, backgrounds, alignment, appearance, biography, level):
    character = Character()
    character.name = name
    character.classs = classs
    character.race = race
    character.sex = sex
    character.backgrounds = backgrounds
    character.alignment = alignment
    character.appearance = appearance
    character.biography = biography
    character.level = level

# TODO: add else fields

    character.save()



def update(self):
    # TODO: update for all fields
    self.save()


def level_up(self):
    # TODO: level_up for character
    self.save()


@staticmethod
def get_all():
    return list(Character.objects.all())
