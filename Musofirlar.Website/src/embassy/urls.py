from django.urls import path
from . import views


urlpatterns = [
    path('embassy/', views.embassy_home, name='embassy_home'),
    path('mobile/embassy/', views.mobile_embassy_home, name='mobile_embassy_home'),
]