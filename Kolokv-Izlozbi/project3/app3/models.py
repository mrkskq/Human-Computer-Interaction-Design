from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# секоја изложба може да содржи повеќе уметнички дела, (1:N)
# еден автор може да има повеќе уметнички дела, (1:N)
# едно дело може да биде прикажано само на една изложба и (1:1) > vekje imat povratna relacija
# едно дело може да биде само на еден автор. (1:1) > vekje imat povratna relacija

class Exhibition(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    style_choices = [
        ("im", "impressionism"),
        ("po", "pop art"),
        ("gr", "graffiti"),
    ]
    style = models.CharField(choices=style_choices, max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.surname}"

class Artwork(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title




