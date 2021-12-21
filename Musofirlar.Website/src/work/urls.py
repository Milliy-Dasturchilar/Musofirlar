from django.urls import path
from . import views

urlpatterns = [
    path('work/', views.work_home, name='work_home'),
    path('mobile/work/', views.mobile_work_home, name='mobile_work_home'),
]
