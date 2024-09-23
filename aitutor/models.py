from django.db import models
import os
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class AITutorChat(models.Model):
    user = models.ForeignKey(User, related_name="ai_users", on_delete=models.CASCADE)
    prompt = models.CharField(max_length=512)
    response = models.TextField(default="")
    created_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("Chat")
        verbose_name_plural = ("Chats")


class AITutorChatSerializer(ModelSerializer):
    class Meta:
        model = AITutorChat
        fields = "__all__"