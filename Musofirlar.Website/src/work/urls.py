from django.url import path
from . import views

urlpatterns = [
    path('work/', views.work_home, name='work_home'),
]