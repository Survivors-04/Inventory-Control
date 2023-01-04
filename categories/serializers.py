from rest_framework import serializers
from .models import Category


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]

    def create(self, validadeted_data: dict) -> Category:
        return Category.objects.create(**validadeted_data)

    def update(self, instance: Category, validated_data: dict) -> Category:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
