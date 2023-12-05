from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse('Email already exists', status=400)

        CustomUser.objects.create_user(email=email,
                                       password=password,
                                       first_name=first_name,
                                       last_name=last_name,
                                       )

        return redirect('congratulation')


def log_in(request):
    if request.method == 'GET':
        return render(request, 'log_in.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('welcome_user') if request.user.role == 0 else redirect('welcome_admin')
        else:
            return HttpResponse('Invalid email or password', status=400)


def log_out(request):
    if request.method == 'POST' and request.user.is_authenticated:
        logout(request)
        return redirect('bye')


# @login_required
# def user_detail(request, user_id=None):
#     user_id = request.POST.get("user_id")
#     if user_id is None:
#         return HttpResponse('Ви забули ввести id користувача!')
#
#     user = CustomUser.get_by_id(user_id=user_id)
#     context = {'user': user}
#     return render(request, 'user_detail.html', context)


