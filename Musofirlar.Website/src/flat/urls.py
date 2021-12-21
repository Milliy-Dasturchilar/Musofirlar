from django.urls import path
from . import views


urlpatterns = [
    path('flat/', views.flat_home, name='flat_home'),
    path('flat-detail/<str:pk>/', views.flat_detail, name='flat_detail'),
    path('flat-create/', views.flat_create, name='flat_create'),

    path('mobile/flat/', views.mobile_flat_home, name='mobile_flat_home'),
]
