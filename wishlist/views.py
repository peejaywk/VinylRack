from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Wishlist
from products.models import Product


@login_required
def wishlist(request):
    """ View to display a user's wishlist """

    # Get the current logged in users wishlist
    # If it doesn't exist then create one.
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add a product to a user's wishlist """

    product = get_object_or_404(Product, pk=product_id)

    # Get the current logged in users wishlist
    # If it doesn't exist then create one.
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]

    wishlist.products.add(product)
    messages.success(request, 'Product added to your wishlist')

    return redirect(reverse('wishlist'))
