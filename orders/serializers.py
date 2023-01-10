from rest_framework import serializers
from .models import Order
from django.shortcuts import get_object_or_404
from .models import Account
from ..products.models import Product
from ..utils.email import SendEmail
import os
import dotenv


dotenv.load_dotenv()


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
            "name_dispatcher",
            "total_price",
        ]
       

    def create(self, validated_data:dict) -> Order:

        products = validated_data.pop("product")
        order = Order.objects.create(**validated_data)
        order.product.set(products)

        return order



    def update(self, instance, validated_data):

        for key, value in validated_data.items():

            if  key == "is_active" or "is_sent":
                setattr(instance, key, value)

        instance.save()


        order_owner = get_object_or_404(Account, pk=self.account_id)
        order_product = get_object_or_404(Product, pk=instance.product.id)
        
        # sender   = self.request.user.email 
        sender = os.getenv("EMAIL_SENDER")
        password_email = os.getenv("APP_PASSWORD")

        adressee = order_owner.email       
        subject  = f"Seu pedido - {order_product.name}"
        
        message  = f"""
            Olá {order_owner.username} gostariamos 
            de informar que seu pedido de id {order_product.id}
            acaba de ser enviado.
        """

        email = SendEmail(
            sender   = sender,
            adressee = adressee,
            subject  = subject,
            message  = message,
            password = password_email,

        )
        email.send()

        return instance
