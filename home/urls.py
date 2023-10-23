from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    # path('login/', views.log_in),
    # path("logout/", views.log_out),
    # path('users/', views.show_all_users),
    # path('user/<int:user_id>/', views.find_user_by_id),
]