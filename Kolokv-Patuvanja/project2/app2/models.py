from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# TouristGuide 1 --- N Travel
# TouristGuide 1 --- 1 User

class TouristGuide(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Travel(models.Model):
    destination = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    guide = models.ForeignKey(TouristGuide, on_delete=models.CASCADE)

    def __str__(self):
        return self.destination



