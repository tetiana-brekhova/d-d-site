from django.contrib import admin
from .models import Languages, Skills, Abilities, Feats

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'language_name']
    search_fields = ['language_name']
    list_filter = ['language_name']


class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'skill_name']
    search_fields = ['skill_name']
    list_filter = ['skill_name']


class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'ability_name', 'get_ability_base']
    search_fields = ['ability_name', 'ability_base']
    list_filter = ['ability_name', 'ability_base']

    def get_ability_base(self, obj):
        return "\n".join([skill.skill_name for skill in obj.ability_base.all()])


class FeatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'feats_name', 'description', 'get_bonus_skill', 'bonus_value']
    search_fields = ['feats_name', 'bonus_skill']
    list_filter = ['feats_name', 'bonus_skill']

    def get_bonus_skill(self, obj):
        return "\n".join([skill.skill_name for skill in obj.bonus_skill.all()])


admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Abilities, AbilitiesAdmin)
admin.site.register(Feats, FeatsAdmin)