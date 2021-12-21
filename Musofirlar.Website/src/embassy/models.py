import os
from uuid import uuid4

from django.db import models

from accounts.models import User


# Create your models here.


class Embassy(models.Model):
    """
    Embassy model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    embassy_name = models.CharField(max_length=50, blank=True, null=True)

    country = models.CharField(max_length=50, blank=True, null=True)

    city = models.CharField(max_length=50, blank=True, null=True)

    address = models.CharField(max_length=200, blank=True, null=True)

    website = models.CharField(max_length=200, blank=True, null=True)

    email = models.CharField(max_length=200, blank=True, null=True)

    phone_number = models.CharField(max_length=200, blank=True, null=True)

    facebook = models.CharField(max_length=200, blank=True, null=True)

    instagram = models.CharField(max_length=200, blank=True, null=True)

    telegram_username = models.CharField(max_length=200, blank=True, null=True)

    telegram_numbers = models.CharField(max_length=200, blank=True, null=True)

    map_link = models.CharField(max_length=200, blank=True, null=True)

    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.embassy_name

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = self.image.name.replace(' ', '')
            self.image.name = self.image.name.replace(',', '-')
            self.image.name = self.image.name.replace('_', '-')
            self.image.name = str(uuid4()) + '-' + self.image.name
        super(Embassy, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(self.image.path)
        super(Embassy, self).delete(*args, **kwargs)
