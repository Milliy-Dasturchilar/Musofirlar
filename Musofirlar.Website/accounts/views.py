from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from accounts.models import User


# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(
            request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Telefon raqam yoki parol noto\'g\'ri'})
    return render(request, 'registration/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {
        'error_messages': [],
    }
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')
        city = request.POST.get('city')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:

            if User.objects.filter(phone_number=phone_number).exists():
                context['error_messages'].append(
                    'Telefon raqam avval ro\'yxatdan o\'tgan')
            elif len(phone_number) < 7:
                context['error_messages'].append(
                    "Telefon raqam to'liq kiritilgan bo'lishi kerak")
            elif len(password1) < 6:
                context['error_messages'].append(
                    "Parol uzunligi kamida 6 ta belgidan iborat bo'lishi kerak")
            if len(country) < 2:
                context['error_messages'].append(
                    "Mamlakat nomi to'liq kiritilgan bo'lishi kerak")
            if len(context['error_messages']) == 0:
                user = User.objects.create_user(
                    phone_number=phone_number,
                    first_name=first_name,
                    last_name=last_name,
                    country=country,
                    city=city,
                    password=password1)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            context['error_messages'].append('Parollar mos kelmadi')
    return render(request, 'registration/register.html', context)