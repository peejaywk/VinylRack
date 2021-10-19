from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Artist, Genre, Recordlabel
from reviews.models import Review


class TestAppModel(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', email='testuser@email.com')
        self.user.set_password('!password1234!')
        self.user.save()

        # Create an Artist
        self.artist = Artist(name="david_bowie", friendly_name='David Bowie')
        self.artist.save()
        # Create a Genre
        self.genre = Genre(name='rock', friendly_name='Rock')
        self.genre.save()
        #Cretae a Record Label
        self.recordlabel = Recordlabel(name='atlantic_records', friendly_name='Atlantic Records')
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

    def test_review_str(self):
        review = Review(
            user=self.user,
            product=self.product,
            review_rating='5',
            review_title='My Album Review',
            review_content='My Album Review Description',
        )

        self.assertEqual(str(review), 'My Album Review')
     
