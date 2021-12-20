from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User


# Register your models here.


admin.site.unregister(Group)
admin.site.register(User)
admin.site.site_header = 'Musofirlar.uz Adminsitration'
admin.site.site_title = 'Musofirlar.uz Adminsitration'
