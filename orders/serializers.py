from rest_framework import serializers
from .models import Order
from products.models import Product
from django.shortcuts import get_object_or_404


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
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
            "account_id",
            "name_dispatcher",
            "total_price",
        ]
       

    def create(self, validated_data:dict) -> Order:
        products = validated_data.pop("product")
        order = Order.objects.create(**validated_data)
        order.product.set(products)
        return order
    
    def update(self, instance: Order, validated_data: dict) -> Order:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
