from .serializers import VideoSerializer,VideoVirtualRealitySerializer, ProductSerializer
from rest_framework import viewsets
from HyGoApp.models import Video, VideoVirtualReality, Product

class VideoViewSet(viewsets.ModelViewSet):
	""" ViewSet for Videos """
	queryset = Video.objects.all()
	serializer_class = VideoSerializer

class TechnicalVideoViewSet(viewsets.ModelViewSet):
	""" ViewSet for videos related to virtual reality and technical videos """
	queryset = VideoVirtualReality.objects.all()
	serializer_class = VideoVirtualRealitySerializer

class ProductViewSet(viewsets.ModelViewSet):
	""" ViewSet for products data """
	queryset = Product.objects.all()
	serializer_class = ProductSerializer