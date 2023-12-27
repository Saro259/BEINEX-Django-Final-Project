from rest_framework import serializers
from products.models import *
from tags.serializer import ReadTagMinSerializer

class WriteProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ['name', 'slug', 'description', 'tags', 'price', 'quantity', 'image']


class ReadProductSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField() #
    class Meta:
        model = Product
        fields = '__all__'

    def get_tags(self, product):
        product_tags = product.tags.all().only('id', 'slug', 'name') 
        return ReadTagMinSerializer(instance=product_tags, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d %B %Y, %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%d %B %H:%M', read_only=True)
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

