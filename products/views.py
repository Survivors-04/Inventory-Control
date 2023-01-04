from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser


class ProductView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = ProductSerializer
    queryset         = Product.objects.all()


    def perform_create(self, serializer:ProductSerializer) -> None:

        serializer.save(account_id=self.request.user.id)


    def get_queryset(self):
        product_id = self.kwargs['pk']
        return self.queryset.filter(produc_id=product_id)

