from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only':True}}

        def create(self, validate_data):
            user_data = CustomUser.objects.create_user(**validate_data)
            return user

