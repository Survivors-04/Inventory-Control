from rest_framework import serializers
from .models import Order


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
            "name_dispatcher",

        ]
        read_only_fields = [
            "id",
            "sent_at",
            "created_at",
            "account_id",
            "name_dispatcher",
        ]

    def create(self, validated_data:dict) -> Order:
        return Order.objects.create(**validated_data)
