from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_student=False, is_teacher=False, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")

        if not password:
            raiseValueError("Users must have a password")

        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password) # change user set_password
        user.student = is_student
        user.teacher = is_teacher
        user.staff = is_staff
        user.admin = is_admin
        user.save(using = self.db)

    def create_studentuser(self,email,password=None):
        user = create_user(
            email,
            password=password,
            is_student=True
        )
        return user

    def create_teacheruser(self,email,password=None):
        user = create_user(
            email,
            password = password,
            is_teacher = True
        )
        return user

    def create_staffuser(self,email,password=None):
        user = create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self,email,password=None):
        user = create_user(
            email,
            password=password,
            is_student=True,
            is_teacher=True,
            is_staff=True,
            is_admin=True
        )
        return user

# Custom User Class definition

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True) #can login
    student = models.BooleanField(default=False)    #student user flag
    teacher = models.BooleanField(default=False)     #teacher user flag not superuser
    staff = models.BooleanField(default=False)      #staff user flag not superuser
    admin = models.BooleanField(default=False)      #superuser
    timestamp = models.DateTimeField(auto_now_add=True) # auto add creation timestamp
    #confirmed = models.BooleanField(default=False) #confirmed Email
    #confirmed_date = models.DateTimeField(default=False) #confirmed date


    objects = UserManager()

    USERNAME_FIELD = 'email' # make email default instead of username
    REQUIRED_FIELDS = []

    def __str__(self):
        return

    @property
    def is_student(self):
        return self.student

    @property
    def is_teacher(self):
        return self.teacher

    @property
    def is_staff(self):
        return self.staff

  # USER_TYPE_CHOICES = (
  #     (1, 'student'),
  #     (2, 'teacher'),
  #     (3, 'secretary'),
  #     (5, 'admin'),
  # )
  #
  # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)


# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     #test = models.ManyToManyField(Test, through='TestDone')
#     #subjects = models.ManyToManyField(Subject, related_name='InterestedinSubject')
#
# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
