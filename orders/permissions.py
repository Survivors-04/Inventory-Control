from rest_framework import permissions
from rest_framework.views import View, Request
from .models import Order
import ipdb


class IsManagerOrOrderOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Order):
        return obj.account == request.user or request.user.is_superuser


# class IsMethodPatchDeleteOrder(permissions.BasePermission):
#     def has_permission(self, request, view:View):
#         if (
#             request.method == "PATCH"
#             and request.user.is_superuser
#             or request.method == "DELETE"
#             and request.user.is_superuser
#         ):
#             return True

class IsMethodPostOrder(permissions.BasePermission):
    def has_permission(self, request: Request, view:View):
            
       for key in request.data:
            if key == "is_active" or "is_sent":
                return True

