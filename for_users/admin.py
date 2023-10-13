from django.contrib import admin
from .models import Race, CharacterClass

class RaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'race_name', 'img_path', 'description',
                    'race_bonus', 'max_age', 'size', 'speed', 'languages', 'else_traits']
    search_fields = ['race_name', 'max_age', 'size', 'speed']
    list_filter = ['race_name', 'max_age', 'size', 'speed']


class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name', 'subclass', 'base_ability', 'img_path', 'description',
                    'full_description', 'advice', 'hit_dice', 'proficiencies', 'ability',
                    'class_equipment', 'base_spell_save_dc', 'spells', 'skills', 'spell_slot']
    search_fields = ['class_name', 'base_ability']
    list_filter = ['class_name', 'base_ability']


admin.site.register(Race, RaceAdmin)
admin.site.register(CharacterClass, ClassAdmin)