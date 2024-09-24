from rest_framework import serializers
from .models import CustomUser, Media


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['media_file'] = instance.media_file.url
        return representation
