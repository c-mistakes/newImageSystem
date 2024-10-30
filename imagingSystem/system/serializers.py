# 序列化处理
from rest_framework import serializers


class ImageResizeSerializer(serializers.Serializer):
    path = serializers.CharField()
    height = serializers.IntegerField()
    width = serializers.IntegerField()
