from django.shortcuts import render
from .models import Canteen

# Create your views here.


def canteen_home(request):
    canteens = Canteen.objects.all()
    return render(request, 'canteen/home.html', {'canteens': canteens})
