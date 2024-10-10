from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import SimpleRouter
from django.contrib.auth import get_user_model
from .models import Quiz, QuizSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()

class QuizView(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
    

router = SimpleRouter(trailing_slash=True)
router.register("quiz", QuizView)