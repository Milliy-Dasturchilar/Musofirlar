from django.urls import path
from . import views


urlpatterns = [
    path('', views.embassy_home, name='embassy_home'),
]