from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from functools import wraps



class Profile(models.Model):
    """
    This models extends the User model storing more information.
    """

    #Connection to User model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #Avatar image
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    #Custom fields for application

    #Basic Details
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    #Details from ForeignKey
    personal_id = models.ForeignKey('Identification', on_delete=models.CASCADE, blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, blank=True,null=True)
    family = models.ForeignKey('Family', on_delete=models.CASCADE, blank=True, null=True)


    #Other Details
    profession = models.CharField(max_length=50, blank=True, null=True)
    personal_email = models.EmailField(verbose_name='personal email address', max_length=255, unique=True, blank=True, null=True)
    personal_website = models.CharField(max_length=30, blank=True, null=True)
    chairs = ArrayField(models.CharField(max_length=4), blank=True,null=True,default=list)
    is_signed = models.BooleanField(default=False)

    #REQUIRED_FIELDS = ['name','surname','birthdate','country']

    def __str__(self):
        return f'{self.user.email} Profile'

    @property
    def get_name(self):
        return self.name

    @property
    def get_surname(self):
        return self.surname

    @property
    def get_coutry(self):
        return self.country

    @property
    def get_id(self):
        return self.personal_id

    @property
    def get_email(self):
        return self.personal_email



class Address(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    freguesia = models.CharField(max_length=30)

class Identification(models.Model):
    ID_TYPE_CHOICES = (('cc','cartao cidadao'),('pp','passport'),)
    #Ids & Fiscal Number
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    id_type = models.CharField(max_length=2, choices=ID_TYPE_CHOICES)
    fiscal_id = models.IntegerField()

class Family(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mothers_name =  models.CharField(max_length=150)
    fathers_name =  models.CharField(max_length=150)


@receiver(post_save, sender=Profile)
def create_or_update_user_profile(sender, instance, **kwargs):
    if not instance:
        return

    if hasattr(instance, '_dirty'):
        return
    #
    # if created:
    #     Profile.objects.create(user=instance)

    else:
        try:
            instance._dirty = True
            instance.save()

        finally:
            del instance._dirty
