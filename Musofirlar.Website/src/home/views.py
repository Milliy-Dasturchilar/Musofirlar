from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Home page view
    """
    return render(request, 'home/home.html')


def mobile_home(request):
    """
    Mobile Home page view
    """
    return render(request, 'mobile/home.html')

