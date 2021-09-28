from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product


class Wishlist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        null=False, blank=False, related_name='wishlist')
    products = models.ManyToManyField(
        Product, through='WishlistItem',
        related_name='wishlist_products')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product.artist.friendly_name
