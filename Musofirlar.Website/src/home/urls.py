from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('mobile/home', views.mobile_home, name='mobile_home'),

    path('', include('src.flat.urls')),
    path('', include('src.work.urls')),
    path('', include('src.canteen.urls')),
    path('', include('src.embassy.urls')),
]
