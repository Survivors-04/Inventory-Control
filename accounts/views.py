from django.shortcuts import render
from .models import Account, CodeRegister
from rest_framework import generics
from .serializers import AccountSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAccountOwner, IsManager



class AccountView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsManager]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class AccountDetailedView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]  

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    lookup_url_kwarg = "pk"

class CodeView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsManager]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

