from django.shortcuts import render
from .models import Account
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AccountSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class AccountView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class AccountDetailedView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    lookup_url_kwarg = "pk"





    
# class AccountView(ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = AccountSerializer

#     def get_queryset(self):
#         return Account.objects.filter(id=self.kwargs["pk"])
        

#     def perform_create(self, serializer):

#         account = get_object_or_404(Account, id=self.kwargs["pk"])
#         serializer.save(account)
    