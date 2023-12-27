from rest_framework import serializers
from orders.models import Order, OrderItems

class ReadOrderItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = '__all__'

class ReadOrderSerializer(serializers.ModelSerializer):

    order_items = serializers.SerializerMethodField()
    def get_order_items(self, object):
        qs = object.order_items.all()
        return ReadOrderItemsSerializer(qs, many=True).data

    class Meta:
        model = Order
        fields = '__all__'
