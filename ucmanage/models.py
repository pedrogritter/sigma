from django.db import models
from django.conf import settings
from userprofiles.models import Profile
# from userauth.models import *

# Create your models here.
class Faculdade(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Departamento(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    fac = models.ForeignKey("Faculdade", on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.name

class Curso(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    abv = models.CharField(max_length=10, blank=True, null=True)
    dep = models.ForeignKey("Departamento", on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.name

class UnidadeCurricular(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    abv = models.CharField(max_length=10, blank=True, null=True)
    cursoID = models.ForeignKey("Curso", on_delete=models.CASCADE, blank=True,null=True)
    # regente = models.ForeignKey("userauth.User", on_delete=models.CASCADE, blank=True,null=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()

    def get_name(self):
        return self.name



class Turno(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    abv = models.CharField(max_length=10, blank=True, null=True)
    ucID =  models.ForeignKey("UnidadeCurricular", on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.name + " | " + self.ucID.name

class Aula(models.Model):
    TYPE_AULA = (('LAB','Laboratorial'),('P','Pratica'),('T','Teorica'),('TP','Teorico-Pratica'))
    DAY_CHOICES = (('Seg','Segunda'),('Ter','Terça'),('Qua','Quarta'),('Qui','Quinta'),('Sex','Sexta'),('Sab','Sabado'), ('Dom','Domingo'))
    type = models.CharField(max_length=3, choices=TYPE_AULA)
    turnoID = models.ForeignKey("Turno", on_delete=models.CASCADE, blank=True,null=True)
    horaINI = models.TimeField()
    horaFIM = models.TimeField()
    diaSemana = models.CharField(max_length=3, choices=DAY_CHOICES)

    def __str__(self):
        return str(self.turnoID) + " - " + self.type

class AlunoAulaUC(models.Model):
    aluno = models.ForeignKey('userprofiles.Profile', on_delete=models.CASCADE, blank=True,null=True)
    uc = models.ForeignKey('UnidadeCurricular', on_delete=models.CASCADE, blank=True,null=True)
    aula = models.ForeignKey('Aula', on_delete=models.CASCADE, blank=True,null=True)

class ProfessorAula(models.Model):
    prof = models.ForeignKey('userprofiles.Profile', on_delete=models.CASCADE, blank=True,null=True)
    aula = models.ForeignKey("Aula", on_delete=models.CASCADE, blank=True,null=True)
    uc = models.ForeignKey("UnidadeCurricular",, on_delete=models.CASCADE, blank=True,null=True)

class PedidoTroca(models.Model):
    aluno = models.ForeignKey('userprofiles.Profile', on_delete=models.CASCADE, blank=True,null=True)
    aula = models.ForeignKey("Aula", on_delete=models.CASCADE, blank=True,null=True)

    STATUS = (('Pendente','Pendente'),('Aceite','Aceite'),('Recusado','Recusado'))
    status = models.CharField(max_length=10, choices=STATUS, default = 'Pendente')
