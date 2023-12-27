from django.db import models
from tags.models import Tags
from authentication.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tags)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.URLField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        db_table = 'reviews'

