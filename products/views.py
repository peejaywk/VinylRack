from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, F

from .models import Product, Artist, Genre, Recordlabel
from reviews.models import Review
from .forms import ProductForm, ArtistForm, RecordLabelForm, GenreForm


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    heading_text = 'All Items'
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            # Sort items by name in ascending or descending order
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
            # Get all Genre objects
            query = request.GET['genre']
            products = products.filter(genre__name__contains=query)
            heading_text = Genre.objects.get(name=query).friendly_name
        if 'artist' in request.GET:
            # Get all Artist objects
            query = request.GET['artist']
            products = products.filter(artist__name__contains=query)
            heading_text = Artist.objects.get(name=query).friendly_name
        if 'label' in request.GET:
            # Get all Record Label objects
            query = request.GET['label']
            products = products.filter(record_label__name__contains=query)
            heading_text = Recordlabel.objects.get(name=query).friendly_name
        if 'on_sale' in request.GET:
            # Get all objects that are marked 'for sale'
            products = products.filter(on_sale=True)
            heading_text = 'Items on Sale!'
        if 'new_in' in request.GET:
            # Get the last 8 objects added to the products table
            products = Product.objects.order_by('-date_added').all()[:8]
            heading_text = 'New In - Latest records added to the store'
        if 'q' in request.GET:
            # Process the search request.
            query = request.GET['q']
            heading_text = 'Search Results'
            if not query:
                messages.error(request, "You didn't enter any search \
                    criteria!")
                return redirect(reverse('products'))

            # Search performed on artist, description and album title.
            queries = Q(artist__name__icontains=query) | \
                Q(description__icontains=query) | \
                Q(album_title__icontains=query)
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

    sum = 0
    count = 0
    avg_rating = 0
    product = get_object_or_404(Product, pk=product_id)

    # Get all reviews associated with the product
    reviews = Review.objects.filter(product=product_id)

    # If the product has reviews then calculate the average review rating
    # for the stars on the product details page.
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
    """ A view to show all available Genres """
    genres = Genre.objects.all().order_by('name')
    template = 'products/genre.html'
    context = {
        'genres': genres,
    }

    return render(request, template, context)


def product_artist(request):
    """ A view to show all available Artists """
    artists = Artist.objects.all().order_by('name')
    template = 'products/artist.html'
    context = {
        'artists': artists,
    }

    return render(request, template, context)


def product_label(request):
    """ A view to show all available Record Labels """
    labels = Recordlabel.objects.all().order_by('name')
    template = 'products/label.html'
    context = {
        'labels': labels,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a new product to the store """

    form = None
    artist_form = None
    record_label_form = None
    genre_form = None

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
            messages.error(request, 'Failed to add product. Please ensure the \
                form is valid.')
    else:
        # Create all forms that the user can populate when adding a new
        # product to the site
        form = ProductForm()
        artist_form = ArtistForm()
        record_label_form = RecordLabelForm()
        genre_form = GenreForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'artist_form': artist_form,
        'record_label_form': record_label_form,
        'genre_form': genre_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product on the site """

    form = None
    product = None
    genre_form = None
    artist = None
    record_label = None

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get all the objects that require a form to be rendered.
    product = get_object_or_404(Product, pk=product_id)
    genre = get_object_or_404(Genre, pk=product.genre_id)
    artist = get_object_or_404(Artist, pk=product.artist_id)
    record_label = get_object_or_404(Recordlabel, pk=product.record_label_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure \
                the form is valid.')
    else:
        # Get data for all forms that the user can edit via the
        # edit product page.
        form = ProductForm(instance=product)
        genre_form = GenreForm(instance=genre)
        artist_form = ArtistForm(instance=artist)
        record_label_form = RecordLabelForm(instance=record_label)
        messages.info(request, f'You are editing {product.album_title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'genre_form': genre_form,
        'artist_form': artist_form,
        'record_label_form': record_label_form,
    }

    return render(request, template, context)


@login_required
def edit_genre(request, genre_id, product_id):
    """ Edit an existing Genre """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    genre = get_object_or_404(Genre, pk=genre_id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated Genre!')
        else:
            messages.error(request, 'Failed to update Genre. Please ensure \
                the form is valid.')

    return redirect(reverse('edit_product', args=[product_id]))


@login_required
def edit_artist(request, artist_id, product_id):
    """ Edit an existing Artist """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated Artist!')
        else:
            messages.error(request, 'Failed to update Artist. Please ensure \
                the form is valid.')

    return redirect(reverse('edit_product', args=[product_id]))


@login_required
def edit_recordlabel(request, label_id, product_id):
    """ Edit an existing Record Label """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    record_label = get_object_or_404(Recordlabel, pk=label_id)
    if request.method == 'POST':
        form = RecordLabelForm(request.POST, instance=record_label)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated Record Label!')
        else:
            messages.error(request, 'Failed to update Record Label. Please ensure \
                the form is valid.')

    return redirect(reverse('edit_product', args=[product_id]))


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

        # Check to see if the artist is already in the database
        artist_name = form['name'].value()
        if Artist.objects.filter(name=artist_name).exists():
            messages.warning(request, 'Artist already exists in the database.')
            return redirect(reverse('add_product'))
        else:
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully added new Artist!')
                return redirect(reverse('add_product'))
            else:
                messages.error(request, 'Failed to add artist. Please ensure \
                    the form is valid.')

    return redirect(reverse('add_product'))


@login_required
def add_recordlabel(request):
    """ Add a record label to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RecordLabelForm(request.POST)

        # Check to see if the label is already in the database
        label_name = form['name'].value()
        if Recordlabel.objects.filter(name=label_name).exists():
            messages.warning(request, 'Record Label already exists in the \
                database.')
            return redirect(reverse('add_product'))
        else:
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully added new Record Label!')
                return redirect(reverse('add_product'))
            else:
                messages.error(request, 'Failed to add record label. \
                    Please ensure the form is valid.')

    return redirect(reverse('add_product'))


@login_required
def add_genre(request):
    """ Add a new genre to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GenreForm(request.POST)

        # Check to see if the label is already in the database
        label_name = form['name'].value()
        if Genre.objects.filter(name=label_name).exists():
            messages.warning(request, 'Genre already exists in the \
                database.')
            return redirect(reverse('add_product'))
        else:
            if form.is_valid():
                form.save()
                messages.info(request, 'Successfully added new Genre!')
                return redirect(reverse('add_product'))
            else:
                messages.error(request, 'Failed to add genre. \
                    Please ensure the form is valid.')

    return redirect(reverse('add_product'))
