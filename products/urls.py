from products.views import CreateProductView, ListProductView, ReviewCreateView, RetrieveListView, ReviewDetailView
from django.urls import path, include

urlpatterns = [
    path('create/',CreateProductView.as_view(), name='create-product'),
    path('list/', ListProductView.as_view(), name='list-product'),
    path('review/<int:product_id>/', ReviewCreateView.as_view(), name='create-product-review'),
    path('review/list/<int:product_id>/', RetrieveListView.as_view(), name= 'review-list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail')
]