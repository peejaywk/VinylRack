from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, F
from django.db.models.functions import Lower
from decimal import Decimal

from .models import Product, Artist, Genre, Recordlabel
from reviews.models import Review
from .forms import ProductForm, ArtistForm, RecordLabelForm


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    heading_text = 'All Items'
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=F('artist__name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'genre' in request.GET:
            query = request.GET['genre']
            products = products.filter(genre__name__contains=query)
            heading_text = Genre.objects.get(name=query).friendly_name
        if 'artist' in request.GET:
            query = request.GET['artist']
            products = products.filter(artist__name__contains=query)
            heading_text = Artist.objects.get(name=query).friendly_name
        if 'label' in request.GET:
            query = request.GET['label']
            products = products.filter(record_label__name__contains=query)
            heading_text = Recordlabel.objects.get(name=query).friendly_name
        if 'on_sale' in request.GET:
            products = products.filter(on_sale=True)
            heading_text = 'Items on Sale!'
        if 'new_in' in request.GET:
            products = Product.objects.order_by('-date_added').all()[:8]
            heading_text = 'New In - Latest records added to the store'
        if 'q' in request.GET:
            query = request.GET['q']
            heading_text = 'Search Results'
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # Search performed on artist, description and album title.
            queries = Q(artist__name__icontains=query) | Q(description__icontains=query) | Q(album_title__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'heading_text': heading_text,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    sale_price = 0
    sum = 0
    count = 0
    avg_rating = 0
    product = get_object_or_404(Product, pk=product_id)

    # Get all reviews associated with the product
    reviews = Review.objects.filter(product=product_id)

    # If the product has reviews then calculate the average review rating
    # for the stars
    if reviews:
        for review in reviews:
            sum += review.review_rating
            count += 1
        avg_rating = sum / count

    template = 'products/product_detail.html'
    context = {
        'product': product,
        'reviews': reviews,
        'review_rating': avg_rating,
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


def product_artist(request):
    """ A view to show all available artists """
    artists = Artist.objects.all()
    template = 'products/artist.html'
    context = {
        'artists': artists,
    }

    return render(request, template, context)


def product_label(request):
    """ A view to show all available record labels """
    labels = Recordlabel.objects.all()
    template = 'products/label.html'
    context = {
        'labels': labels,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        artist_form = ArtistForm()
        record_label_form = RecordLabelForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'artist_form': artist_form,
        'record_label_form': record_label_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.album_title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_artist(request):
    """ Add a artist to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added artist!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add artist. Please ensure the form is valid.')

    return redirect(reverse('add_product'))


@login_required
def add_recordlabel(request):
    """ Add a record label to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RecordLabelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added record label!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add record label. Please ensure the form is valid.')

    return redirect(reverse('add_product'))
