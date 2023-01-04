from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Account(AbstractUser):
    name = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    email = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=12, null=True)
