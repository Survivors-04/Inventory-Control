from rest_framework import serializers
from .models import Category

class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]