from django.urls import path
from . import views


app_name = 'charactermaker'

urlpatterns = [
    path('', views.charactermaker, name="charactermaker"),
    path('page/', views.page, name="page"),

]



