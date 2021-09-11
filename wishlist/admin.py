from django.contrib import admin
from .models import Wishlist, WishlistItem


class WishlistItemAdminInline(admin.TabularInline):
    model = WishlistItem


class WishlistAdmin(admin.ModelAdmin):
    inlines = (WishlistItemAdminInline,)

    fields = ('user',)

    list_display = ('user',)


admin.site.register(Wishlist, WishlistAdmin)
