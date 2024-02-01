from django.urls import path
from . import views

app_name = 'charactermaker'

urlpatterns = [
    path('', views.charactermaker, name="charactermaker"),
    path('personality_creation/', views.personality_creation, name="personality_creation"),
    path('spells_chooser/', views.spells_chooser, name="spells_chooser"),
    path('confirm_character/', views.confirm_character, name="confirm_character"),

]
