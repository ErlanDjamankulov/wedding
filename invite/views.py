from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions
class PhotoViewSets(viewsets.ModelViewSet):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer
class MusicViewSets(viewsets.ModelViewSet):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer
class TimeViewSets(viewsets.ModelViewSet):
	queryset = Time.objects.all()
	serializer_class = TimeSerializer
class GuestViewSets(viewsets.ModelViewSet):
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer
