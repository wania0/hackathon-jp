from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate

from .serializers import UserSerializer, SignupSerializer, LoginSerializer

@api_view(['POST'])
def signup_view(request : Request):
    data = request.data
    serializer = SignupSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        data['password'] = make_password(data['password'])
        # data['is_staff'] = 1
        # data['is_superuser'] = 1
        User.objects.create(**data)
    else:
        return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
    return Response("success")

@api_view(['POST'])
def login_view(request:Request):
    data = request.data
    serializer = LoginSerializer(data=data)
    
    if serializer.is_valid():
        data = serializer.validated_data
        user = authenticate(request, username=data['username'], password=data['password'])
        
        if user is not None:
            login(request, user)
            return Response("user logged in")
        else: 
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request: Request):
    logout(request)
    return Response("log out!!!!!!")


@api_view(['GET'])
def profile_view(request: Request):
    if request.user.is_authenticated:
        user = UserSerializer(request.user)
        return Response(user.data)
    else:
        return Response("please login")
    
    
    