from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from products.serializers import *
from products.permissions import IsReviewAuthorOrReadOnly
from django.utils.text import slugify
from rest_framework.generics import ListAPIView
from products.models import Product
from products.filters import SimplePaginationClass
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
# Create your views here.

class CreateProductView(APIView):
    """To create the product object - the product description, price, quantity, tag which it is associated"""
    def post(self, request):
        request_data = request.data
        request_data.update({'slug': slugify(request_data.get('name'))})
        serializer = WriteProductSerializer(data=request_data)
        if serializer.is_valid():
            product_instance = serializer.save()
            response_data = ReadProductSerializer(instance=product_instance).data
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListProductView(ListAPIView):
    """List of all the products present in the database of Ecommerce API"""
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer
    pagination_class = SimplePaginationClass
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    # ordering = ['-id']
    ordering_fields = ['id', 'created_at']
    search_fields = ['^name']
    filterset_fields = ['price', 'tags']


class ReviewCreateView(generics.CreateAPIView):
    """To create the review object for the desired product/product id and to permit the review author"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        review_author = self.request.user

        serializer.save(product=product, review_author=review_author)

class RetrieveListView(generics.ListAPIView):
    """Retrieves and lists all reviews associated with a specific product."""
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        return Review.objects.filter(product=product)

    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """"Retrieves, updates, or deletes a specific review, with access restricted
    to the review author or read-only access for others."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]