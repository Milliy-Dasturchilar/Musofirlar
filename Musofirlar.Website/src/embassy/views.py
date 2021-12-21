from django.shortcuts import render

# Create your views here.

def emabssy_home(request):
    return render(request, 'embassy/index.html')
