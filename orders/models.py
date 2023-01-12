from django.db import models
import uuid
from products.models import Product
from accounts.models import Account


class Order(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at      = models.DateField(auto_now_add=True, null=False)
    sent_at         = models.DateField(null=True)
    total_price     = models.DecimalField(max_digits=10, decimal_places=2)
    amount          = models.IntegerField(null=False)
    is_active       = models.BooleanField(default=True)
    is_sent         = models.BooleanField(default=False)
    name_dispatcher = models.CharField(max_length=100, null=False)
    account         = models.ForeignKey(Account, on_delete=models.CASCADE)
    product         = models.ManyToManyField("products.Product", related_name="products_orders")
