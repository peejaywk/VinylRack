from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Product


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


def add_review(request, product_id):
    """ A view to add a new product review """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_title = form.cleaned_data['review_title']
            review_content = form.cleaned_data['review_content']
            Review.objects.create(
                user=request.user,
                product=product,
                review_title=review_title,
                review_content=review_content
            )
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('list_reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'product': product,
    }
    template = 'reviews/add_review.html'
    return render(request, template, context)
