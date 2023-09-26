from django.urls import path
from . import views


app_name = 'usersguid'

urlpatterns = [
    path('races/', views.races, name="races"),
    path('classes/', views.classes, name="classes"),
    path('personality/', views.personality, name="personality"),
    path('equipment/', views.equipment, name="equipment"),
    path('magic/', views.magic, name="magic"),
    path('charactermaker/', views.charactermaker, name="charactermaker"),
    path('usersguid/', views.usersguid, name="usersguid")
]

