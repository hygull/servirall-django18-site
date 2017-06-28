from HyGoApp.models import Video, VideoVirtualReality, Product, FishImage
from rest_framework import serializers

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer class for Videos """
	class Meta:
		model = Video
		fields = "__all__"

class VideoVirtualRealitySerializer(serializers.HyperlinkedModelSerializer):
	""" Serializer class for Videos related to virtual reality and other technical videos """
	class Meta:
		model = VideoVirtualReality
		fields = "__all__"

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer class for flipkart/amazon/wallmart like products """
	class Meta:
		model = Product
		fields = "__all__"

class FishImageSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer class for flipkart/amazon/wallmart like products """
	class Meta:
		model = FishImage
		fields = "__all__"