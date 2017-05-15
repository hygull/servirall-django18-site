from HyGoApp.models import Video
from rest_framework import serializers

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer class for Videos"""
	class Meta:
		model = Video
		fields = "__all__"
