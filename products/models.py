from django.db import models
import uuid
from categories.models import Category
from accounts.models import Account

class Product(models.Model):
    
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=100, unique=True, null=False)
    description = models.CharField(max_length=255, null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    amount      = models.IntegerField(null=False)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_id")
    account     = models.ForeignKey(Account, on_delete=models.CASCADE)
