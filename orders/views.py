from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, DestroyAPIView
from tags.models import Tags
from tags.serializer import WriteTagSerializer, ReadTagSerializer
from django.utils.text import slugify
from django.core.cache import cache
from products.filters import SimplePaginationClass
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import transaction
from products.models import Product
from orders.models import Order, OrderItems
from orders.serializers import ReadOrderItemsSerializer, ReadOrderSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CreateOrderView(APIView):
    """For creating the order for the consumer according to product name, qty, payment mode etc."""
    def post(self, request):
        orders = request.data.get('orders')
        payment_mode = request.data.get('payment_mode')
        payment_status = request.data.get('payment_status')
        user_id = request.user.id
        with transaction.atomic():
            order = Order.objects.create(
                user_id = user_id,
                payment_mode = payment_mode,
                payment_status = payment_status,
                payment_amount = 0
            )
            total_amount = 0
            product_id = orders.get("product_id")
            qty = orders.get("qty")
            product_id = int(product_id)
            product = Product.objects.get(pk=product_id)
            qty = min(product.quantity, int(qty))
            total_amount += product.price * qty
            OrderItems.objects.create(
                product_id = product_id,
                order_id = order.id,
                price = product.price,
                quantity=qty
            )
            order.payment_amount = total_amount
            payment_status = 2
            order.save()
            response_data = ReadOrderSerializer(instance=order).data
            return Response(response_data, status=status.HTTP_200_OK)


class OrderListView(ListAPIView):
    """Details of the order created for the particular consumer"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializers = ReadOrderSerializer(orders, many=True)
        return Response(serializers.data)