from django.urls import path
from .views import FirebaseTokenCreateView, SendNotificationView

urlpatterns = [
    path("register-token/", FirebaseTokenCreateView.as_view(), name="register_token"),
    path("send-notification/", SendNotificationView.as_view(), name="send_notification"),
]
