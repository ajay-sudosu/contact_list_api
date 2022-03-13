from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100,write_only=True)
    email = serializers.EmailField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']


    def validate_username(self,username):
        if User.objects.filter(username=username).exists():
            raise ValidationError({'message':'user is already present'})
        return username


    def validate(self,attrs):
        if User.objects.filter(email=attrs.get('email')).exists():
            raise ValidationError({'message':'email in use'})
        return attrs
        

    def create(self,validate_data):
        return User.objects.create_user(**validate_data)



class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100,write_only=True)

    class Meta:
        model = User
        fields = ['username','password']