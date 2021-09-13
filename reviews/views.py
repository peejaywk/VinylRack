from django.shortcuts import render, get_object_or_404
from .models import Review


def list_reviews(request):
    """ View to display a list of reviews """

    if request.GET:
        if 'product' in request.GET:
            product_id = request.GET['product']
            reviews = Review.objects.filter(product=product_id)
            print('Product')
            print(reviews)
    else:
        reviews = Review.objects.filter(user=request.user)

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }
    return render(request, template, context)
