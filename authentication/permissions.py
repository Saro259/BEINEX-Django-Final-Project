from rest_framework.permissions import BasePermission
from authentication.models import User
from django.conf import settings



class IsAuthenticatedAndActiveUser(BasePermission):
    """To Authenticate the account whether the user is active or not."""
    message = "Invalid token or user"

    def has_permission(self, request, view):
        request_user = request.user
        return isinstance(request_user, User) and (request_user.is_active == True)

class IsAdmin(BasePermission):
    """To Authenticate the account whether the user is a staff or a consumer through is_superuser boolean."""
    message = "Invalid token or user"

    def has_permission(self, request, view):
        request_user = request.user
        return isinstance(request_user, User) and (request_user.is_superuser == True)