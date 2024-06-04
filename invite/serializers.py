from rest_framework import serializers
from .models import GuestResponse

class GuestResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestResponse
        fields = ['name', 'message', 'attending']