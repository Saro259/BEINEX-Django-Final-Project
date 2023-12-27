from rest_framework import permissions

class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """To provide the permission to the consumer who has given their review over the product"""
    def has_object_permission(self, request, obj, view):
        if request.method is permissions.SAFE_METHODS:
            return True
        return obj.review_author == request.user