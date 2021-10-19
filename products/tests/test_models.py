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
