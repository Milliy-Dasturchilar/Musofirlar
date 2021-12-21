from django.shortcuts import render


# Create your views here.


def embassy_home(request):
    return render(request, 'embassy/index.html')
