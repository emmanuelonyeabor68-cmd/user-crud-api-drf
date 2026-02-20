from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Users must be at least 18 years old.")
        return value 