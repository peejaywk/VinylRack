from django.contrib import admin
from .models import Genre, Artist, Product, Recordlabel


admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Product)
admin.site.register(Recordlabel)
