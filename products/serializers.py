from rest_framework import serializers
from categories.serializers import CategorySerilizer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Product
        
        fields = [
            "id",
            "name",
            "description",
            "price",
            "amount",
            "category",
            "account_id",
        ] 
        
        read_only_fields = ["id", "account_id"]
        depth = 1
    
    def create(self, validated_data:dict)-> Product:
        
        return Product.objects.create(**validated_data)


    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance