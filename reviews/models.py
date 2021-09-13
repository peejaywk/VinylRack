from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=False, blank=False, related_name='review')

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        null=False, blank=False, related_name='product')

    created_on = models.DateTimeField(default=timezone.now)

    review_title = models.CharField(max_length=254, null=False, blank=False)
    review_content = models.TextField(max_length=1200, null=False, blank=False, default='')

    def __str__(self):
        return self.review_title
