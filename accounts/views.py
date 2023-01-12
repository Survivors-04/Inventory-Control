from .models import Account
from rest_framework import generics
from .serializers import AccountSerializer, LoginSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAccountOwner, IsManager
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class AccountView(generics.ListCreateAPIView):
   
    serializer_class = AccountSerializer
    queryset         = Account.objects.all()



class AccountDetailedView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated, IsAccountOwner]  

    serializer_class = AccountSerializer
    queryset         = Account.objects.all()

    lookup_url_kwarg = "pk"


class LoginView(APIView):

    def post(self, request: Request) -> Response:

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = authenticate(
            email    = serializer.validated_data["email"],
            password = serializer.validated_data["password"],
        )

        if not account:
            return Response(
                {"detail": "invalid credentials"},
                status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(account)
        token = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        
        return Response(token)





