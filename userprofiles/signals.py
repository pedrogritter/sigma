from django.conf import settings
from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from userauth.models import User
from django.dispatch import receiver
from .models import Profile

# #Auto creates
# @receiver(post_save, sender=User)
# def create_address(sender, instance, created, **kwargs):
#     if created:
#         Address.objects.create(user.instance)
#
# @receiver(post_save, sender=User)
# def create_identification(sender, instance, created, **kwargs):
#     if created:
#         Identification.objects.create(user.instance)
#
# @receiver(post_save, sender=User)
# def create_family(sender, instance, created, **kwargs):
#     if created:
#         Family.objects.create(user.instance)
#
#
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
#
# # Auto Saves
#
# @receiver(post_save, sender=User)
# def save_address(sender, instance, **kwargs):
#         instance.address.save()
#
# @receiver(post_save, sender=User)
# def save_identification(sender, instance, **kwargs):
#         instance.personal_id.save()
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#         instance.family.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()
