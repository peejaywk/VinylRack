from django.shortcuts import render


def wishlist(request):
    template = 'wishlist/wishlist.html'
    context = {}
    return render(request, template, context)
