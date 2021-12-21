from django.urls import path
from . import views


urlpatterns = [
    path('', views.canteen_home, name='canteen_home'),
]