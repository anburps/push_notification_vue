from rest_framework import serializers
from .models import FirebaseToken

class FirebaseTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseToken
        fields = '__all__'
