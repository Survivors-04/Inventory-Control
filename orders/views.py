from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerOrOrderOwner
from accounts.permissions import IsManager

from ..utils.email import SendEmail


class OrderManagerView(generics.UpdateAPIView,generics.DestroyAPIView, generics.ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated, IsManager]

    serializer_class = OrderSerializer
    queryset         = Order.objects.all()
    

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class OrderUserView(generics.CreateAPIView, generics.RetrieveAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated, IsManagerOrOrderOwner]

    serializer_class = OrderSerializer


    def get_queryset(self):

        if self.request.method is "POST" and not self.request.user.is_superuser:
            return Order.objects.all()
            
        return Order.objects.all()

