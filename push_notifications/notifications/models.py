from django.db import models

class FirebaseToken(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.token}"
