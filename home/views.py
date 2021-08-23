from django.shortcuts import render
from products.models import Product


def index(request):
    """
    A view to return the index page.
    """
    products = Product.objects.order_by('artist').all()
    template = 'home/index.html'
    context = {
        'products': products,
    }
    return render(request, template, context)
