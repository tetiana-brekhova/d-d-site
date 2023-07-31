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
        middle_name = request.POST.get('middle_name')
        role = request.POST.get('role')

        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse('Email already exists', status=400)

        if role == 'admin':
            CustomUser.objects.create_superuser(email=email,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name,
                                                middle_name=middle_name
                                                )

        if role == 'user':
            CustomUser.objects.create_user(email=email,
                                           password=password,
                                           first_name=first_name,
                                           last_name=last_name,
                                           middle_name=middle_name
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


@login_required
def user_list(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'user_list.html', context)


@login_required
def user_detail(request, user_id=None):
    user_id = request.POST.get("user_id")
    if user_id is None:
        return HttpResponse('Ви забули ввести id користувача!')

    user = CustomUser.get_by_id(user_id=user_id)
    context = {'user': user}
    return render(request, 'user_detail.html', context)


@login_required
def return_user_manager(request):
    if request.method == 'POST':
        return render(request, 'user_manager.html')


@login_required
def return_author_manager(request):
    if request.method == 'POST':
        return render(request, 'author_manager.html')


@login_required
def return_order_manager(request):
    if request.method == 'POST':
        return render(request, 'order_manager.html')


@login_required
def return_book_manager(request):
    if request.method == 'POST':
        return render(request, 'book_manager.html')













