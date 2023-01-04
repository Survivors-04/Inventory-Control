from rest_framework.generics import ListCreateAPIView
from .serializers import OrderSerializer
from .models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser


class OrderView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAdminUser]

    serializer_class = OrderSerializer
    queryset         = Order.objects.all()


    def perform_create(self, serializer):
        serializer.save(account=self.request.user)
    

    def get_queryset(self):
        order_id = self.kwargs['pk']
        return self.queryset.filter(id=order_id)