# your_app/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User

class GoogleLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

    def create(self, validated_data):
        # Create or update the user based on the provided data
        user, created = User.objects.update_or_create(
            email=validated_data['email'],
            defaults={'username': validated_data['username']}
        )
        return user
