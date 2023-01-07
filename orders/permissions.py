from rest_framework import permissions
from rest_framework.views import View, Request
from .models import Order

class IsManagerOrOrderOwner(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj:Order):
        return obj.account == request.user or request.user.is_superuser
