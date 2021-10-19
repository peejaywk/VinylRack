from django.test import TestCase
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from products.models import Product, Artist, Genre, Recordlabel
from django.conf import settings


class TestAppModel(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com'
        )
        self.user.set_password('!password1234!')
        self.user.save()

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
            price=19.99,
            on_sale=False,
            discount_percent=0,
            image=None,
            image_url='/media/123.jpg',
            media_condition='VG',
            sleeve_condition='VG',
            cat_num='12345-abcde',
        )
        self.product.save()

        # Create an order
        self.order = Order(
            order_number='1234567890',
            full_name='John Smith',
            email='john.smith@email.com',
            phone_number='5551234',
            street_address1='12 Main Street',
            street_address2='Top Flat',
            town_or_city='York',
            county='Yorkshire',
            postcode='YH106DQ',
            country='UK',
            delivery_cost=0,
            order_total=0,
            grand_total=0,
            original_bag='1234',
            stripe_pid='123456',
        )
        self.order.save()

    def test_order_str(self):
        self.assertEqual(str(self.order), '1234567890')

    def test_orderlineitem_str(self):
        orderlineitem = OrderLineItem(
            order=self.order,
            product=self.product,
            quantity=1,
        )
        orderlineitem.save()
        self.assertEqual(str(orderlineitem), 'SKU p1234567 on order 1234567890')

    def test_orderlineitem_save(self):
        """
        Tests that the lineitem_total is updated when the save method
        is called.
        """
        orderlineitem = OrderLineItem(
            order=self.order,
            product=self.product,
            quantity=1,
        )
        orderlineitem.save()

        total = orderlineitem.quantity * self.product.price
        self.assertEqual(orderlineitem.lineitem_total, total)

        # Change quantity to 2 and call save method
        # Check the lineitem_total has been updated.

        orderlineitem = OrderLineItem(
            order=self.order,
            product=self.product,
            quantity=2,
        )
        orderlineitem.save()

        total = orderlineitem.quantity * self.product.price
        self.assertEqual(orderlineitem.lineitem_total, total)

    def test_order_update_total(self):
        """
        Test the update_total method in the order model.
        """
  
        orderlineitem = OrderLineItem(
            order=self.order,
            product=self.product,
            quantity=2,
        )
        orderlineitem.save()

        delivery_cost = (
            self.order.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100)      
        grand_total = self.order.order_total + delivery_cost
        self.order.update_total()

        self.assertEqual(self.order.delivery_cost, delivery_cost)
        self.assertEqual(self.order.grand_total, grand_total)
