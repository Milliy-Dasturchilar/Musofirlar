from django.urls import path
from . import views


urlpatterns = [
    path('', views.emabssy_home, name='emabssy_home'),
]