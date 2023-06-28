import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        
        token = auth_data.decode('utf-8').split(' ')[0]

        try:
            payload = jwt.decode(token,settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(username=payload.get('username'))
            return user, token
 
        except jwt.DecodeError as e_:
            raise exceptions.AuthenticationFailed('token is invalid')

        except jwt.ExpiredSignatureError as e_:
            raise exceptions.AuthenticationFailed('token is expired')
