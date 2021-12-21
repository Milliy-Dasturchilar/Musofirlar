from django.shortcuts import render
from .models import Embassy


# Create your views here.


def embassy_home(request):
    embassies = Embassy.objects.all()
    return render(request, 'embassy/embassy.html', {'embassies': embassies})


def mobile_embassy_home(request):
    embassies = Embassy.objects.all()
    return render(request, 'mobile/embassy.html', {'embassies': embassies})

