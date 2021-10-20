from django.test import TestCase
from products.models import Product, Artist, Genre, Recordlabel


class TestAppModel(TestCase):
    """ Unit tests for the products app models """
    def setUp(self):
        # Create an Artist
        self.artist = Artist(name="david_bowie", friendly_name='David Bowie')
        self.artist.save()
        # Create a Genre
        self.genre = Genre(name='rock', friendly_name='Rock')
        self.genre.save()
        # Cretae a Record Label
        self.recordlabel = Recordlabel(
            name='atlantic_records',
            friendly_name='Atlantic Records')
        self.recordlabel.save()
        # Create a Product
        self.product = Product(
            sku='p1234567',
            genre=self.genre,
            artist=self.artist,
            record_label=self.recordlabel,
            album_title='Legacy',
            description='Double album released in 2017',
            price='19.99',
            on_sale=False,
            discount_percent='0',
            image=None,
            image_url='/media/123.jpg',
            media_condition='VG',
            sleeve_condition='VG',
            cat_num='12345-abcde',
        )
        self.product.save()

    def test_artist_str(self):
        """
        Test to check the correct string is returned by the __str__ and
        get_friendly_name methods in the Artist model
        """
        artist = Artist.objects.get(pk=self.artist.id)
        expected_result = artist.name
        self.assertEqual(str(self.artist), expected_result)

        expected_result = artist.friendly_name
        self.assertEqual(self.artist.get_friendly_name(), expected_result)

    def test_genre_str(self):
        """
        Test to check the correct string is returned by the __str__ and
        get_friendly_name methods in the Genre model
        """
        genre = Genre.objects.get(pk=self.genre.id)
        expected_result = genre.name
        self.assertEqual(str(self.genre), expected_result)

        expected_result = genre.friendly_name
        self.assertEqual(self.genre.get_friendly_name(), expected_result)

    def test_recordlabel_str(self):
        """
        Test to check the correct string is returned by the __str__ and
        get_friendly_name methods in the Recordlabel model
        """
        recordlabel = Recordlabel.objects.get(pk=self.recordlabel.id)
        expected_result = recordlabel.name
        self.assertEqual(str(self.recordlabel), expected_result)

        expected_result = recordlabel.friendly_name
        self.assertEqual(
            self.recordlabel.get_friendly_name(),
            expected_result
        )

    def test_product_str(self):
        """
        Test to check the correct string is returned by the __str__ method
        in the Product model
        """
        product = Product.objects.get(pk=self.product.id)
        expected_result = product.album_title
        self.assertEqual(str(self.product), expected_result)

    # Check that the values of the field labels are correct
    def test_genre_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_genre_friendly_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_artist_name_label(self):
        artist = Artist.objects.get(id=1)
        field_label = artist._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_artist_friendly_name_label(self):
        artist = Artist.objects.get(id=1)
        field_label = artist._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_recordlabel_name_label(self):
        recordlabel = Recordlabel.objects.get(id=1)
        field_label = recordlabel._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_recordlabel_friendly_name_label(self):
        recordlabel = Recordlabel.objects.get(id=1)
        field_label = recordlabel._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_product_album_title_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('album_title').verbose_name
        self.assertEqual(field_label, 'album title')

    def test_product_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_product_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_product_on_sale_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('on_sale').verbose_name
        self.assertEqual(field_label, 'on sale')

    def test_product_discount_percent_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('discount_percent').verbose_name
        self.assertEqual(field_label, 'discount percent')

    def test_product_image_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_product_image_url_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('image_url').verbose_name
        self.assertEqual(field_label, 'image url')

    def test_product_media_condition_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('media_condition').verbose_name
        self.assertEqual(field_label, 'media condition')

    def test_product_sleeve_condition_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('sleeve_condition').verbose_name
        self.assertEqual(field_label, 'sleeve condition')

    def test_product_cat_num_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('cat_num').verbose_name
        self.assertEqual(field_label, 'cat num')

    def test_product_date_added_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('date_added').verbose_name
        self.assertEqual(field_label, 'date added')

    # Check that the size of the character fields are correct.
    def test_genre_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_genre_friendly_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_artist_name_max_length(self):
        artist = Artist.objects.get(id=1)
        max_length = artist._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_artist_friendly_name_max_length(self):
        artist = Artist.objects.get(id=1)
        max_length = artist._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_recordlabel_name_max_length(self):
        recordlabel = Recordlabel.objects.get(id=1)
        max_length = recordlabel._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_recordlabel_friendly_name_max_length(self):
        recordlabel = Recordlabel.objects.get(id=1)
        max_length = recordlabel._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_product_album_title_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('album_title').max_length
        self.assertEqual(max_length, 254)

    def test_product_image_url_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('image_url').max_length
        self.assertEqual(max_length, 1024)

    def test_product_media_condition_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('media_condition').max_length
        self.assertEqual(max_length, 16)

    def test_product_sleeve_condition_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('sleeve_condition').max_length
        self.assertEqual(max_length, 16)

    def test_product_cat_num_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('cat_num').max_length
        self.assertEqual(max_length, 254)

    def test_product_price_max_digits(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('price').max_digits
        self.assertEqual(max_length, 6)

    def test_product_price_decimal_places(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('price').decimal_places
        self.assertEqual(max_length, 2)

    def test_product_discount_percent_max_digits(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('discount_percent').max_digits
        self.assertEqual(max_length, 2)

    def test_product_discount_percent_decimal_places(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('discount_percent').decimal_places
        self.assertEqual(max_length, 0)
