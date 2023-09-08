# Imports from rest_framework
from rest_framework import serializers
# Import get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'email', 'first_name',
              'last_name', 'is_staff', 'is_active', 'get_full_name', 'get_short_name')
