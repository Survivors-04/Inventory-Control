from rest_framework import permissions
from rest_framework.views import View, Request
from accounts.models import Account

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj:Account):
        return obj == request.user
        
class IsManager(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj: Account):
        return obj == request.user.is_superuser