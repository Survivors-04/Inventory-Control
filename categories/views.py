from django.shortcuts import render

from .models import Category
from .serializers import CategorySerilizer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerilizer
    queryset = Category.objects.all()

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    
    serializer_class = CategorySerilizer
    queryset = Category.objects.all()


    