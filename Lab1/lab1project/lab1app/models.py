from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORIES = {
        "CA": "Cardio",
        "YO": "Yoga",
        "ST": "Strength"
    }
    category_name = models.CharField(max_length=3, choices=CATEGORIES)
    category_description = models.CharField(max_length=100)
    is_highly_demanded = models.BooleanField(default=False)
    def __str__(self):
        return self.category_name

class Instructor(models.Model):
    EXPERIENCE_LEVELS = {
        "BE": "Beginner",
        "CE": "Certified",
        "PT": "Professional Trainer"
    }
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    biography = models.TextField()
    experience_level = models.CharField(max_length=3, choices=EXPERIENCE_LEVELS)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Training(models.Model):
    training_name = models.CharField(max_length=30)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    price_per_training_session = models.IntegerField()
    number_of_available_spots = models.IntegerField()
    def __str__(self):
        return self.training_name