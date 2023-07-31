from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.register),
    # path('/', views.sign_up),
    path("logout/", views.log_out),
    # path('users/', views.show_all_users),
    # path('user/<int:user_id>/', views.find_user_by_id),
]