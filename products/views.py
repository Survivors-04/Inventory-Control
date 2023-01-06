from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductView(generics.ListAPIView ):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    serializer_class = ProductSerializer
    queryset         = Product.objects.all()


    def perform_create(self, serializer:ProductSerializer) -> None:
        serializer.save(account_id=self.request.user.id)


class ProductDetailView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    serializer_class = ProductSerializer

    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Product.objects.all()

