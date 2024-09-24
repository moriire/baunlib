from django.db import models
import os
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class AITutorChat(models.Model):
    class SubjectChoices(models.TextChoices):
        iot = "IOT"
        coding = "CODING"
        stem = "STEM"
        robotics = "ROBOTICS"
        ai = "AI"
    user = models.ForeignKey(User, related_name="ai_users", on_delete=models.CASCADE)
    subject = models.CharField(max_length=9, choices=SubjectChoices)
    prompt = models.CharField(max_length=512)
    response = models.TextField(default="")
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.prompt

    class Meta:
        verbose_name = ("Chat")
        verbose_name_plural = ("Chats")

class AITutorChatSerializer(ModelSerializer):
    class Meta:
        model = AITutorChat
        fields = ("user", "subject", "prompt", "response", "id")