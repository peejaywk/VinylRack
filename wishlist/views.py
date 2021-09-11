from django.shortcuts import render, get_object_or_404
from .models import Wishlist, WishlistItem
from profiles.models import UserProfile


def wishlist(request):
    """ View to display a users wishlist """
    
    # Get the current logged in users wishlist
    # If it doesn't exist then create one.
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }
    return render(request, template, context)
