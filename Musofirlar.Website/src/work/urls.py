from django.urls import path
from . import views

urlpatterns = [
    path('work/', views.work_home, name='work_home'),
]
