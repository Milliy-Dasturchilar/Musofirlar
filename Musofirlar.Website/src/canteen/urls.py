from django.urls import path
from . import views


urlpatterns = [
    path('canteen/', views.canteen_home, name='canteen_home'),
]