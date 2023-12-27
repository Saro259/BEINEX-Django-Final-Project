from rest_framework import serializers
from tags.models import Tags

class WriteTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']

class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields =['id', 'name', 'slug', 'created_at', 'updated_at']

class ReadTagMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name', 'slug']

