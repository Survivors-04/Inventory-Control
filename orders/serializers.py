from rest_framework import serializers
from rest_framework.views import  Request, Response, status
from .models import Order
from django.shortcuts import get_object_or_404
from .models import Account
from products.models import Product
from utils.email import SendEmail
import os
import dotenv
import ipdb
import json

dotenv.load_dotenv()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "created_at",
            "is_active",
            "amount",
            "sent_at",
            "is_sent",
            "account_id",
            "total_price",
            "product",
        ]
        read_only_fields = [
            "id",
            "sent_at",
            "created_at",
            "name_dispatcher",
            "total_price",
        ]


def create(self, validated_data: dict) -> Order:
    products = validated_data.pop("product")
    order = Order.objects.create(**validated_data)
    order.product.set(products)
    return order


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "is_active",
            "is_sent",
            "account_id",
            "name_dispatcher",
            "product",
            
        ]
        read_only_fields = ["id", "total_price", "sent_at", "product", "name_dispatcher"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "is_active" or "is_sent" or "name_dispatcher":
               setattr(instance, key, value)
        instance.save()

        order_owner = get_object_or_404(Account, pk=self["account_id"].value)
        
        products = []
        for product_id in self["product"].value:
            product =  get_object_or_404(Product, pk=product_id)
            products.append(product.name)
            
   
        sender = os.getenv("EMAIL_SENDER")
        password_email = os.getenv("APP_PASSWORD")
        adressee = order_owner.email   
        subject = f"Seu pedido - "
        for prod in products:
                subject  += f"{prod}"
        
        id_order = self["id"]
        message = f" Olá {order_owner.username} gostariamos de informar que seu pedido de  {id_order} acaba de ser enviado."
        email = SendEmail(
            sender=sender,
            addressee=adressee,
            subject=subject,
            message=message,
            password=password_email,
        )
        email.send()
        return instance


