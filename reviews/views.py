from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Product


def list_reviews(request):
    """ View to display a list of reviews """

    hide_image = False
    if request.GET:
        if 'product' in request.GET:
            product_id = request.GET['product']
            reviews = Review.objects.filter(product=product_id)
            hide_image = True
    else:
        reviews = Review.objects.filter(user=request.user)

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
        'hide_image': hide_image,
    }
    return render(request, template, context)


@login_required
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


@login_required
def edit_review(request, review_id):
    """ Edit a product review """

    review = get_object_or_404(Review, pk=review_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, 'Successfully edited review!')
            return redirect(reverse('list_reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        # Check to see the logged in user is the original author of the
        # review post. If not rediret
        if review.user != request.user:
            messages.error(request, 'You cannot edit this review as you are not the original author.')
            # Get the url the request has been made from so the
            # user can be redirected to that page
            previous_url = request.META.get('HTTP_REFERER')
            return redirect(previous_url)
        form = ReviewForm(instance=review)

    context = {
        'form': form,
    }
    template = 'reviews/edit_review.html'
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a prodproduct review """

    review = get_object_or_404(Review, pk=review_id)
    if review.user != request.user:
        messages.error(request, 'You cannot delete this review as you are not the original author.')
        # Get the url the request has been made from so the
        # user can be redirected to that page
        previous_url = request.META.get('HTTP_REFERER')
        return redirect(previous_url)
    else:
        review.delete()
        messages.success(request, 'Review deleted!')
        return redirect(reverse('list_reviews'))
