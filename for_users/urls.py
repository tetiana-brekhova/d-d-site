from django.urls import path
from . import views


app_name = 'usersguid'

urlpatterns = [
    path('races/', views.races, name="races"),
    path('races/<race>/', views.show_race, name='race'),
    path('classes/', views.classes, name="classes"),
    path('classes/<classs>/', views.show_class, name='class'),
    path('personality/', views.personality, name="personality"),
    path('equipment/', views.equipment, name="equipment"),
    path('magic/', views.magic, name="magic"),
    path('magic/<class_id>', views.class_spells, name="class_spells"),
    path('usersguid/', views.usersguid, name="usersguid"),
    path('languages/', views.languages, name="languages")

]



