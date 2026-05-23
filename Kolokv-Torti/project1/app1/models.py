from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Baker 1 --- N Cake
# Baker 1 --- 1 User

class Baker(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True) # otposle dodaeno

    def __str__(self):
        return f"{self.name} {self.surname}"

class Cake(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name