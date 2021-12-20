from django.shortcuts import render

# Create your views here.


def home(request):
    """
    Home page view
    """
    return render(request, 'home/home.html')
