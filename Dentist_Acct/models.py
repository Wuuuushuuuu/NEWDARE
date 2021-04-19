from django.db import models

# Create your models here.
class Dentist_Acct(models.Model):
    Name = models.TextField()
    Username = models.TextField()
    Password = models.TextField()
    Clients = models.TextField()
