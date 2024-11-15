from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255)
    car_type = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    dealer = models.CharField(max_length=100)

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')
