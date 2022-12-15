from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(sender, instance, created, kwargs, "SIGNAL")
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()