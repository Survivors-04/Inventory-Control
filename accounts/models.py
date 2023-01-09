from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Account(AbstractUser):

    name = models.CharField(max_length=100, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=12)
    
    


