from django.db import models
from userprofiles.models import Profile
from ucmanage.models import Aula
# Create your models here.
class Presenca(models.Model):
    aula = models.ForeignKey("ucmanage.Aula", on_delete=models.CASCADE, blank=True,null=True)
    aluno = models.ForeignKey('userprofiles.Profile', on_delete=models.CASCADE, blank=True,null=True)
    date = models.DateField()
