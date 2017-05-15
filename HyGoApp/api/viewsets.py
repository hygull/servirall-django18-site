from .serializers import VideoSerializer
from rest_framework import viewsets
from HyGoApp.models import Video

class VideoViewSet(viewsets.ModelViewSet):
	""" """
	queryset = Video.objects.all()
	serializer_class = VideoSerializer