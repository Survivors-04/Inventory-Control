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
            "username",
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

    def create(self, validated_data):
        if validated_data["is_superuser"] == True:
            return Account.objects.create_superuser(**validated_data)

        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):

    email    = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser

