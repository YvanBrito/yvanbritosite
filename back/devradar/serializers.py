from rest_framework import serializers
from devradar.models import Dev


class DevSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    github_username = serializers.CharField(max_length=30)
    bio = serializers.CharField(max_length=300, allow_blank=True)
    avatar_url = serializers.CharField(max_length=100)
    techs = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Dev.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.github_username = validated_data.get('github_username', instance.github_username)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar_url = validated_data.get('avatar_url', instance.avatar_url)
        instance.techs = validated_data.get('techs', instance.techs)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance