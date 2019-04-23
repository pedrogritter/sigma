from django.db import models
from django.conf import settings
# Create your models here.
class Faculdade(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

class Departamento(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    fac = models.ForeignKey("Faculdade", on_delete=models.CASCADE, blank=True,null=True)

class Curso(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    abv = models.CharField(max_length=10, blank=True, null=True)
    dep = models.ForeignKey("Departamento", on_delete=models.CASCADE, blank=True,null=True)

class UnidadeCurricular(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    abv = models.CharField(max_length=10, blank=True, null=True)
    cursoID = models.ForeignKey("Curso", on_delete=models.CASCADE, blank=True,null=True)
    #regente
    year = models.IntegerField()

class Turno(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    abv = models.CharField(max_length=10, blank=True, null=True)
    ucID =  models.ForeignKey("UnidadeCurricular", on_delete=models.CASCADE, blank=True,null=True)

class Aula(models.Model):
    TYPE_AULA = (('Lab'),('Pratica'),('Teorica'))
    DAY_CHOICES = (('Segunda'),('Terça'),('Quarta'),('Quinta'),('Sexta'),('Sabado'), ('Domingo'))
    type = models.CharField(max_length=1, choices=TYPE_AULA)
    turnoID = models.ForeignKey("Turno", on_delete=models.CASCADE, blank=True,null=True)
    horaINI = models.TimeField()
    horaFIM = models.TimeField()
    diaSemana = models.CharField(max_length=1, choices=DAY_CHOICES)

class Presenca(models.Model):
    aulaID = models.ForeignKey("Aula", on_delete=models.CASCADE, blank=True,null=True)
    alunoID = models.ForeignKey(settings.Profile, on_delete=models.CASCADE, blank=True,null=True)
    date = models.DateField()
