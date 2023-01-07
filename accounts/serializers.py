from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from .models import Account, CodeRegister

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

class CodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CodeRegister
        fields = [
            "id",
            "code",
            "account_id",
        ]
        read_only_fields = ["id", "account_id"]