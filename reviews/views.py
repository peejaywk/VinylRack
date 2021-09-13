from django.shortcuts import render, get_object_or_404
from .models import Review


def list_reviews(request):
    """ View to display a list of reviews """

    reviews = Review.objects.filter(user=request.user)
    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }
    return render(request, template, context)
