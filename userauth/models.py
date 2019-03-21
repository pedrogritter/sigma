from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'secretary'),
      (5, 'admin'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #test = models.ManyToManyField(Test, through='TestDone')
    #subjects = models.ManyToManyField(Subject, related_name='InterestedinSubject')

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
