from django.shortcuts import render
from authentication.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import auth
from rest_framework.generics import ListAPIView
from authentication.serializers import ReadUserSerializer
from django.conf import settings
from django.core.cache import cache
from authentication.mailer import send_registered_mail
from authentication.permissions import IsAuthenticatedAndActiveUser, IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class SignUpView(APIView):

    """The Sign Up Functionality for the user. The Sign Up account gets authenticated 
    and receives an account activated mail."""
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        if not username:
            return Response({'error': True, 'msg': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({'error': True, 'msg': 'Email id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': True, 'msg': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error': True, 'msg': 'This email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=username, email=email, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            send_registered_mail(email)
            return Response({'success': True, 'msg': 'Authentication done! try signing back with same credentials'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': True, 'msg': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

class UserListView(ListAPIView):
    """List of all accounts registered will be displayed. 
    It will only be displayed to the user if is_staff boolean is true and the token is valid."""
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ReadUserSerializer
    def get_queryset(self):
        print('request user id', self.request.user.id)
        print('request user username', self.request.user.username)
        queryset = User.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

