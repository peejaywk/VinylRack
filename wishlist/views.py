from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Wishlist, WishlistItem
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

    # Get the url the request has been made from so the
    # user can be redirected to that page
    previous_url = request.META.get('HTTP_REFERER')

    # Get the current logged in users wishlist
    # If it doesn't exist then create one.
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]

    in_wishlist =  WishlistItem.objects.filter(wishlist=wishlist, product=product).exists()

    if in_wishlist:
        messages.info(request, 'Product is already in your wishlist')
    else:
        wishlist.products.add(product)
        messages.success(request, 'Product added to your wishlist')

    return redirect(previous_url)


@login_required
def delete_from_wishlist(request, product_id):
    """ Delete a product from a user's wishlist """

    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get(user=request.user)

    wishlist.products.remove(product)

    messages.success(request, 'Product deleted from your wishlist')

    return redirect(reverse('wishlist'))
