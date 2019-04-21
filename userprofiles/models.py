from django.conf import settings
from django.db import models


class Profile(models.Model):

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
