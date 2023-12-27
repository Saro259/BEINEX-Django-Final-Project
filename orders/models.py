from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _
from products.models import Product
from model_utils import Choices


PAYMENT_MODES = Choices(
    (1, 'cod', _('COD')),
    (2, 'card', _('Card')),
    (3, 'upi', _('UPI')),
    (4, 'netbanking', _('NetBanking'))
)

PAYMENT_STATUS = Choices (
    (1, 'pending', _('pending')),
    (2, 'completed', _('completed'))
)

TRACK_STATUS = (
    ('ordered', _('Ordered')),
    ('shipped', _('Shipped'))
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_amount = models.IntegerField(default=0)
    payment_mode = models.IntegerField(choices=PAYMENT_MODES, default=PAYMENT_MODES.cod)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS, default=PAYMENT_STATUS.pending)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20, choices=TRACK_STATUS, default='ordered')

    class Meta:
        db_table = 'Order'

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=TRACK_STATUS, default='ordered')

    class Meta:
        db_table = 'OrderItems'