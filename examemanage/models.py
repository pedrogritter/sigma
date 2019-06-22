from django.db import models
from django.conf import settings
from userprofiles.models import Profile
from ucmanage.models import *

# Create your models here.
class Exame(models.Model):
    ucID = models.ForeignKey('ucmanage.UnidadeCurricular', on_delete=models.CASCADE, blank=True,null=True)
    horaINI = models.TimeField()
    Duracao = models.TimeField()
    date = models.DateField()




class ExameAluno(models.Model):
    exameID = models.ForeignKey("Exame", on_delete=models.CASCADE, blank=True,null=True)
    alunoID = models.ForeignKey('userprofiles.Profile', on_delete=models.CASCADE, blank=True,null=True)
    
