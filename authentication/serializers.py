from rest_framework.serializers import ModelSerializer
from authentication.models import User


class ReadUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active', 'is_superuser')
        