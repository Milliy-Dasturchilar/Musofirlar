from django.shortcuts import render

# Create your views here.


def canteen_home(request):
    return render(request, 'canteen/home.html')