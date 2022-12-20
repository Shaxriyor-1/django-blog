from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(sender, instance, created, kwargs, "SIGNAL")
    if created:
        user_profile = Profile(user=instance, firstname=instance.first_name, lastname=instance.last_name)
        user_profile.save()


@receiver(post_save, sender=User)
def edit_profile(sender, instance, created, **kwargs):
    print(sender, instance, created, kwargs, "SIGNAL")
    if created:
        user_profile = Profile(user=instance, firstname=instance.first_name, lastname=instance.last_name)
        user_profile.save()


