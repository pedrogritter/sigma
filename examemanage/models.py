from django.db import models
from django.conf import settings
from userprofiles.models import Profile
from ucmanage.models import UnidadeCurricular

# Create your models here.
class Exame(models.Model):
    ucID = models.ForeignKey('ucmanage.UnidadeCurricular', blank=True,null=True)
    horaINI = models.TimeField()
    horaFim = models.TimeField()
    date = models.DateField()


class ExameAluno(models.Model):
    exameID = models.ForeignKey("examemanage.Exame", blank=True,null=True)
    alunoID = models.ForeignKey('userprofiles.Profile', blank=True,null=True)
    inscrito = models.BooleanField(default=False)
