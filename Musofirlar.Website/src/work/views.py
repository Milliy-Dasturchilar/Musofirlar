from django.shortcuts import render

# Create your views here.

def work_home(request):
    return render(request, 'work/work_home.html')