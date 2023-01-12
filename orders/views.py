from rest_framework.views import  Request, Response, status
from rest_framework import generics
from .serializers import OrderSerializer, OrderUpdateSerializer
from .models import Order
from products.models import Product
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerOrOrderOwner, IsMethodPostOrder
from .error.errors import InvalidValueUpdate
from accounts.permissions import IsManager
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

        for id in self.request.data["product"]:
            prod = get_object_or_404(Product, id=id)
            amount_x_price = prod.price * self.request.data["amount"]

        serializer.save(account=self.request.user, 
                        total_price=amount_x_price)


class OrderDetailView(generics.RetrieveDestroyAPIView):
    
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class SendOrderView(generics.UpdateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()

    def perform_update(self, serializer):
        
        if self.request.data["is_active"] == True or self.request.data["is_sent"] == False:
            
            raise InvalidValueUpdate("não é possivel atualizar este campo")
        
        serializer.save(name_dispatcher=self.request.user.username)
