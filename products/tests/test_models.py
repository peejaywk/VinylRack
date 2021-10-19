from django.test import TestCase
from products.models import Product, Artist, Genre, Recordlabel
from django.contrib.auth.models import User


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
        self.assertEqual(str(self.artist), 'david_bowie')
        self.assertEqual(self.artist.get_friendly_name(), 'David Bowie')

    def test_genre_str(self):
        self.assertEqual(str(self.genre), 'rock')
        self.assertEqual(self.genre.get_friendly_name(), 'Rock')

    def test_recordlabel_str(self):
        self.assertEqual(str(self.recordlabel), 'atlantic_records')
        self.assertEqual(
            self.recordlabel.get_friendly_name(),
            'Atlantic Records'
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Legacy')
