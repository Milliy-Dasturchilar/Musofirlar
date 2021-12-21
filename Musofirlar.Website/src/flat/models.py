import os

from django.db import models
from accounts.models import User
from uuid import uuid4


# Create your models here.


class Flat(models.Model):
    """
    Flat model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    country = models.CharField(max_length=50, blank=True, null=True)

    city = models.CharField(max_length=50, blank=True, null=True)

    address = models.CharField(max_length=200, blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    room_count = models.IntegerField(blank=True, null=True)

    floor = models.CharField(max_length=50, blank=True, null=True)

    image = models.ImageField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.author.first_name}\'s flat in {self.country} {self.city} {self.address}'

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = self.image.name.replace(' ', '')
            self.image.name = self.image.name.replace(',', '-')
            self.image.name = self.image.name.replace('_', '-')
            self.image.name = str(uuid4()) + '-' + self.image.name
        super(Flat, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(self.image.path)
        super(Flat, self).delete(*args, **kwargs)
