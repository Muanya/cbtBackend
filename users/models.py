from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    reg_no = models.CharField('Identification Number', max_length=15, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'reg_no'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.reg_no

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Department(models.Model):
    name = models.CharField(unique=True, max_length=100)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Students(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.IntegerField()
    # passport = models.CharField()  # base64 encoded string
    # finger_print = models.CharField()
    reg_date = models.DateTimeField('date registered', auto_now_add=True)

    def __str__(self):
        return self.user.__str__()


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    reg_date = models.DateTimeField('date registered', auto_now_add=True)

    def __str__(self):
        return self.user.__str__()
