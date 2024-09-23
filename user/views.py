from djoser.views import TokenCreateView
from rest_framework.response import Response
from rest_framework import status

class CustomTokenCreateView(TokenCreateView):
    def _action(self, serializer):
        user = serializer.user
        token = self.token_model.objects.create(user=user)
        return Response(
            {
                'auth_token': token.key,
                'user_id': user.id,
                'username': user.username
            },
            status=status.HTTP_200_OK
        )
