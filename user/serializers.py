from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth import get_user_model
import json
User = get_user_model()

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['id'] = user.id
        return token
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = json.dumps({
            'id': self.user.id,
            'username': self.user.username
        })
        return data