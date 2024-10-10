from django.db import models
import os
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class Quiz(models.Model):
    class SubjectChoices(models.TextChoices):
        iot = "IOT"
        coding = "CODING"
        stem = "STEM"
        robotics = "ROBOTICS"
        ai = "AI"
    user = models.ForeignKey(User, related_name="quiz_users", on_delete=models.CASCADE)
    subject = models.CharField(max_length=9, choices=SubjectChoices)
    grade = models.CharField(max_length=6)
    score = models.IntegerField(default=0)
    modified_on = models.DateTimeField(auto_now_add = True)
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
    
    
    def remarks(self):
        msg =""
        if self.score >=80:
            msg = "Excellent"
        elif 60 >= self.score >=79:
            msg = "Very Good"
        elif 50 >= self.score >=59:
            msg = "Good"
        else:
            msg = "Pass"
        return msg

    class Meta:
        verbose_name = ("Quiz")
        verbose_name_plural = ("Quizes")

class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("id", "user", "subject", "grade", "score", "remarks")