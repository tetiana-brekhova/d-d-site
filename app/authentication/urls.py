from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.register),
    path('log_in', views.log_in),
    path("logout/", views.log_out),
]