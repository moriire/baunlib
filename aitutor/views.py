from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import SimpleRouter
from django.contrib.auth import get_user_model
from .models import AITutorChat, AITutorChatSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .quiz_files import stx, read_file

User = get_user_model()

class AITutorView(ModelViewSet):
    queryset = AITutorChat.objects.all()
    serializer_class = AITutorChatSerializer

    @action(methods=("POST",), detail=False)
    def quiz(self, request, *a, **kw):
        data = request.data
        print(data)
        x = read_file()
        return Response(data=x)

router = SimpleRouter(trailing_slash=True)
router.register("tutor", AITutorView)