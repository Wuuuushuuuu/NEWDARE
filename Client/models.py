from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import CharField

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, contact_no, name, password=None):
        if not name:
            raise ValueError("Users must enter their full name")
        if not email:
            raise ValueError("Users must enter their email")
        if not contact_no:
            raise ValueError("Users must enter their working contact number")

        user = self.model(
            name = name, 
            email = self.normalize_email(email),
            contact_no = contact_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, contact_no, name, password):
        user = self.create_user(
            name = name, 
            email = self.normalize_email(email),
            contact_no = contact_no,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class client(AbstractBaseUser):
    name = models.CharField(verbose_name="Name", max_length=100, unique=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=60)
    contact_no = models.CharField(verbose_name="Contact number",max_length=12)
    date_joined = models.DateTimeField(verbose_name=" Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['contact_no','email']

    objects = MyUserManager()

    def __str__(self):
        return (self.name + "," + self.contact_no)
    
    def has_perm(self, perm, obj =None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Records(models.Model):
    Name = models.CharField(max_length=60)
    Email = models.EmailField()
    Contact_no = models.CharField(max_length=20)

COLOR_CHOICES = (
    ('Pending','Pending'),
    ( 'Confirmed','Confirmed'),
)


class Bookings(models.Model):
    Name = models.CharField(max_length=60)
    Contact_no = models.CharField(max_length=20)
    Date = models.DateField()
    Concern = models.CharField(max_length=60)
    time = models.CharField(max_length=60)
    Status = models.CharField(max_length=30, choices=COLOR_CHOICES, default='Pending')

class Logged_in(models.Model):
    Name = models.CharField(max_length=60)
    Contact_no = models.CharField(max_length=20)