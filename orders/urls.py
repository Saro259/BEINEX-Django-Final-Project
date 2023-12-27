from django.urls import path
from orders.views import CreateOrderView, OrderListView

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create_order'),
    path('list/', OrderListView.as_view(), name='order_list'),
]