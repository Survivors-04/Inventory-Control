from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from .models import Account

class AccountSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
    validators=[
        UniqueValidator(queryset=Account.objects.all(), message= "This field must be unique.")]
    )

    cpf = serializers.CharField(
    validators=[
        UniqueValidator(queryset=Account.objects.all(), message= "This field must be unique.")]
    )

    class Meta:
        model = Account
        fields = [
            "id",
            "name",
            "cpf",
            "email",
            "telephone",
            "password",
            "is_superuser"
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only":True}
        }



class LoginSerializer(serializers.Serializer):

    email    = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser

