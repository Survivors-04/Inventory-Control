from rest_framework import serializers
from .models import Order
from django.shortcuts import get_object_or_404
from .models import Account

from products.models import Product
from utils.email import Email
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
            "product",
        ]
        read_only_fields = ["id", "total_price", "sent_at", "product"]


    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            if key == "is_active" or "is_sent":
                setattr(instance, key, value)
        instance.save()

        order_owner = get_object_or_404(Account, id=self["account_id"].value)
        
        product_id = self['product'].value[0]
        product    =  get_object_or_404(Product, pk=product_id)
            
        subject = f"Seu pedido - {product.name}"
        
        order_id = self["id"].value

        email = Email(
            adressee=order_owner,
            subject=subject,
            order_id=order_id
        )
        email.send()
        
        return instance