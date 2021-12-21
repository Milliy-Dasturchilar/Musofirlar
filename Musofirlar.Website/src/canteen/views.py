from django.shortcuts import render
from .models import Canteen

# Create your views here.


def canteen_home(request):
    canteens = Canteen.objects.all()
    return render(request, 'canteen/canteen.html', {'canteens': canteens})


def mobile_canteen_home(request):
    canteens = Canteen.objects.all()
    return render(request, 'mobile/canteen.html', {'canteens': canteens})
