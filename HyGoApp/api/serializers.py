from HyGoApp.models import Video, VideoVirtualReality
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