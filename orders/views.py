from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order
from products.models import Product

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerOrOrderOwner, IsMethodPatchDeleteOrder, IsMethodPostOrder
from accounts.permissions import IsManager
from django.shortcuts import get_object_or_404
import ipdb


class OrderView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):
        
        if self.request.method == "GET" and self.request.user.is_superuser :
            return Order.objects.all()
        return Order.objects.filter(account=self.request.user)
        

    def perform_create(self, serializer):

        serializer.save(account=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated, IsMethodPatchDeleteOrder]

    serializer_class = OrderSerializer
    queryset         = Order.objects.all()