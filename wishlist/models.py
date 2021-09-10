from django.db import models
from django.utils import timezone
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    user = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE,
        null=False, blank=False, related_name='wishlist')

    def __str__(self):
        return self.user.user.username


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product.album_title
