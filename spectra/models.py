from django.db import models
from django.contrib.auth.models import User


class SmartPhone(models.Model):
    phone_name = models.CharField(max_length=500)
    phone_desc1 = models.CharField(max_length=10000)
    phone_desc2 = models.CharField(max_length=10000)
    phone_desc3 = models.CharField(max_length=10000)
    phone_desc4 = models.CharField(max_length=10000)
    phone_picture = models.CharField(max_length=1000)
    release_date = models.CharField(max_length=500)
    dimensions = models.CharField(max_length=500)
    primary_camera = models.CharField(max_length=50)
    secondary_camera = models.CharField(max_length=50)
    ram = models.CharField(max_length=20)
    storage = models.CharField(max_length=20)
    os = models.CharField(max_length=200)
    processor = models.CharField(max_length=1000)
    battery = models.CharField(max_length=200)
    water_resistant = models.BooleanField()

    def __str__(self):
        return self.phone_name


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_name = models.CharField(max_length=500)
    datetime = models.CharField(max_length=100)
    comment = models.CharField(max_length=50000)
