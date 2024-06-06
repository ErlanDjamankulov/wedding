from rest_framework import serializers
from .models import *
class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Photo
		fields='__all__'
class MusicSerializer(serializers.ModelSerializer):
	class Meta:
		model=Music
		fields='__all__'
class TimeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Time
		fields='__all__'
class GuestSerializer(serializers.ModelSerializer):
	class Meta:
		model=Guest
		fields='__all__'