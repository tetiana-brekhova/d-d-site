from django.urls import path
from . import views


app_name = 'usersguid'

urlpatterns = [
    path('languages/', views.languages, name="languages"),
    path('skills/', views.skills, name="skills"),
    path('abilities/', views.abilities, name="abilities"),
    path('feats/', views.feats, name="feats"),

]

