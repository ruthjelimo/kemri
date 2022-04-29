# from knox.models import AuthToken
# from .serializers import UserSerializer
# from django.contrib.auth import login
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView
# from rest_framework.authtoken import views as authviews
# from rest_framework import permissions
# from rest_framework.response import Response
# from django.shortcuts import render




# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         # serializer = AuthTokenSerializer(data=request.data)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         # serializer = AuthTokenSerializer(data=request.data)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)


from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from core.serializers import (
    SellerCustomRegistrationSerializer, BuyerCustomRegistrationSerializer
    )

class SellerRegistrationView(RegisterView):
    serializer_class = SellerCustomRegistrationSerializer


class BuyerRegistrationView(RegisterView):
    serializer_class = BuyerCustomRegistrationSerializer
