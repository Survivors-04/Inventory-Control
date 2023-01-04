from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    email = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=100, null=False)
    is_superuser = models.BooleanField(default=False)