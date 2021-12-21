from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        counrty = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        try:
            price = int(request.POST.get('price'))
        except:
            price = 0
        try:
            room_count = int(request.POST.get('room_count'))
        except:
            room_count = 0
        description = request.POST.get('description')
        floor = request.POST.get('floor')
        image = request.FILES.get('image')
        new_flat = Flat(
            author=request.user,
            country=counrty,
            city=city,
            address=address,
            price=price,
            room_count=room_count,
            description=description,
            floor=floor,
            image=image,
        )
        new_flat.save()
        return redirect('flat_detail', pk=new_flat.pk)
    return render(request, 'flat/ijara-uy-qoshish.html')


def mobile_flat_home(request):
    flats = Flat.objects.all()[::-1]
    context = {
        'flats_top': flats[:3],
        'flats_all': flats,
    }
    return render(request, 'mobile/flat.html', context)