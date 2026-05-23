import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from app2.models import *


# Кога се брише турситичкиот водач, неговите дестинации по случаен избор се додаваат на остатите туристички водачи

@receiver(pre_delete, sender=TouristGuide)
def my_handler(sender, instance, **kwargs):
    destinations = Travel.objects.filter(guide = instance)
    other_guides = TouristGuide.objects.exclude(id = instance.id).all()

    for dest in destinations:
        new_guide = random.choice(other_guides)
        dest.guide = new_guide
        dest.save()

# registriraj go signalot vo apps.py vo def ready funkcijata