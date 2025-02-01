from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FirebaseToken
from .serializers import FirebaseTokenSerializer

class FirebaseTokenCreateView(generics.CreateAPIView):
    queryset = FirebaseToken.objects.all()
    serializer_class = FirebaseTokenSerializer
    permission_classes = [IsAuthenticated]


import firebase_admin
from firebase_admin import messaging

def send_push_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token,
    )
    response = messaging.send(message)
    return response

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FirebaseToken

class SendNotificationView(APIView):
    def post(self, request):
        title = request.data.get("title")
        body = request.data.get("body")
        tokens = FirebaseToken.objects.values_list("token", flat=True)

        for token in tokens:
            send_push_notification(token, title, body)

        return Response({"message": "Notification sent successfully"})
