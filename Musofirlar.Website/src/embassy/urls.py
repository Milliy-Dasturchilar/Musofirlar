from django.urls import path
from . import views


urlpatterns = [
    path('embassy/', views.embassy_home, name='embassy_home'),
]