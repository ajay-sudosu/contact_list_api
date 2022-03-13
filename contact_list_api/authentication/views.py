from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializer import UserSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from django.contrib.auth.models import User

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = auth.authenticate(username=username,password=password)
        if user:
            print('yes user present')
            auth_token = jwt.encode({'username':user.username},settings.SECRET_KEY)
            serializer = UserSerializer(user)

            data= {'user':serializer.data,
            'token':auth_token}
            return Response(data)
        return Response({'message':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)





