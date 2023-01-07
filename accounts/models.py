from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Account(AbstractUser):

    name = models.CharField(max_length=100, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=12)
    
    
class CodeRegister(models.Model):
    code = models.IntegerField(null=False)
    account = models.OneToOneField("accounts.Account", on_delete=models.CASCADE, related_name="account_id")

