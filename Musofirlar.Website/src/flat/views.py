from django.shortcuts import render
from .models import Flat

# Create your views here.


def flat_home(request):
    flats = Flat.objects.all()[::-1]
    context = {
        'flats_top': flats[:3],
        'flats_all': flats,
    }
    return render(request, 'flat/flat.html', context)


def flat_detail(request, pk):
    flat = Flat.objects.filter(pk=pk).first()
    context = {
        'flat': flat,
    }
    return render(request, 'flat/flat-detail.html', context)


def flat_create(request):
    pass
    # return render(request, 'flat/flat-create.html')
