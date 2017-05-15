from .serializers import VideoSerializer,VideoVirtualRealitySerializer
from rest_framework import viewsets
from HyGoApp.models import Video, VideoVirtualReality

class VideoViewSet(viewsets.ModelViewSet):
	""" ViewSet for Videos """
	queryset = Video.objects.all()
	serializer_class = VideoSerializer

class TechnicalVideoViewSet(viewsets.ModelViewSet):
	""" ViewSet for videos related to virtual reality and technical videos """
	queryset = VideoVirtualReality.objects.all()
	serializer_class = VideoVirtualRealitySerializer