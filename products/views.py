from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Product, Artist, Genre


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'genre' in request.GET:
            query = request.GET['genre']
            products = products.filter(genre__name__contains=query)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # Search performed on artist, description and album title.
            queries = Q(artist__name__icontains=query) | Q(description__icontains=query) | Q(album_title__icontains=query)
            print(queries)
            print(products)
            products = products.filter(queries)

    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


def product_genre(request):
    """ A view to show all available genres """
    genres = Genre.objects.all()
    template = 'products/genre.html'
    context = {
        'genres': genres,
    }

    return render(request, template, context)
