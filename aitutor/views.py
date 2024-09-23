from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import SimpleRouter
from django.contrib.auth import get_user_model
from .models import AITutorChat, AITutorChatSerializer

User = get_user_model()

class AITutorView(ModelViewSet):
    queryset = AITutorChat.objects.all()
    serializer_class = AITutorChatSerializer

router = SimpleRouter(trailing_slash=True)
router.register("tutor", AITutorView)