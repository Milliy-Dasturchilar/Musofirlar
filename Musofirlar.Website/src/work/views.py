from django.shortcuts import render
from .models import Work

# Create your views here.


def work_home(request):
    works = Work.objects.all()
    return render(request, 'work/work.html', {'works': works})


def mobile_work_home(request):
    works = Work.objects.all()
    return render(request, 'mobile/work.html', {'works': works})
