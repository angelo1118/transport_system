from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
     


class Car(models.Model):
    model_name = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255, null=True)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.model_name
