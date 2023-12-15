from django.urls import path
from . import views

app_name = 'charactermaker'

urlpatterns = [
    path('', views.charactermaker, name="charactermaker"),
    path('page/', views.page, name="page"),
    path('page2/', views.page2, name="page2"),
    # path('character/', views.character, name="character"),

]
