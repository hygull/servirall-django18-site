from .serializers import VideoSerializer,VideoVirtualRealitySerializer, ProductSerializer, FishImageSerializer
from rest_framework import viewsets
from HyGoApp.models import Video, VideoVirtualReality, Product, FishImage

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

class FishImageViewSet(viewsets.ModelViewSet):
	""" ViewSet for products data """
	queryset = FishImage.objects.all()
	serializer_class = FishImageSerializer