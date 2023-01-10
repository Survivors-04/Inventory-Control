from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import Account
class BackendEmail(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Account.objects.get(Q(username__iexact=email) | Q(email__iexact=email))
        except Account.DoesNotExist:
            Account().set_password(password)
            return
        except Account.MultipleObjectsReturned:
            user = Account.objects.filter(Q(username__iexact=email) | Q(email__iexact=email)).order_by('id').first()
        if user.check_password(password) and self.user_can_authenticate(user):
            return user