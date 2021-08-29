from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Artist(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Recordlabel(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, default="", blank=True)
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(
        'Artist', null=True, blank=True, on_delete=models.SET_NULL)
    record_label = models.ForeignKey(
        'Recordlabel', null=True, blank=True, on_delete=models.SET_NULL)
    album_title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField()
    discount_percent = models.DecimalField(max_digits=2, decimal_places=0)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, default="", blank=True)
    media_condition = models.CharField(max_length=16)
    sleeve_condition = models.CharField(max_length=16)
    cat_num = models.CharField(max_length=254, default="", blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.album_title
