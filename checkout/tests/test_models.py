from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from products.models import Product, Artist, Genre, Recordlabel


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
        """
        Test to check the correct string is returned by the __str__ method
        in the Order model
        """
        order = Order.objects.get(pk=self.order.id)
        expected_result = order.order_number
        self.assertEqual(str(self.order), expected_result)

    def test_orderlineitem_str(self):
        """
        Test to check the correct string is returned by the __str__ method
        in the OrderLineItem model
        """
        orderlineitem = OrderLineItem(
            order=self.order,
            product=self.product,
            quantity=1,
        )
        orderlineitem.save()

        expected_result = f'SKU {orderlineitem.product.sku} on order {orderlineitem.order.order_number}'
        self.assertEqual(str(orderlineitem), expected_result)

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

    # Check that the values of the field labels are correct
    def test_order_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_number').verbose_name
        self.assertEqual(field_label, 'order number')

    def test_user_profile_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user_profile').verbose_name
        self.assertEqual(field_label, 'user profile')

    def test_full_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full name')

    def test_email_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_phone_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')

    def test_country_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('country').verbose_name
        self.assertEqual(field_label, 'country')

    def test_postcode_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('postcode').verbose_name
        self.assertEqual(field_label, 'postcode')

    def test_town_or_city_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('town_or_city').verbose_name
        self.assertEqual(field_label, 'town or city')

    def test_street_address1_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('street_address1').verbose_name
        self.assertEqual(field_label, 'street address1')

    def test_street_address2_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('street_address2').verbose_name
        self.assertEqual(field_label, 'street address2')

    def test_county_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('county').verbose_name
        self.assertEqual(field_label, 'county')

    def test_date_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_delivery_cost_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('delivery_cost').verbose_name
        self.assertEqual(field_label, 'delivery cost')

    def test_order_total_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_total').verbose_name
        self.assertEqual(field_label, 'order total')

    def test_grand_total_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('grand_total').verbose_name
        self.assertEqual(field_label, 'grand total')

    def test_original_bag_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('original_bag').verbose_name
        self.assertEqual(field_label, 'original bag')

    def test_stripe_pid_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('stripe_pid').verbose_name
        self.assertEqual(field_label, 'stripe pid')

    # Check that the size of the character fields are correct.
    def test_order_number_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_number').max_length
        self.assertEqual(max_length, 32)

    def test_full_name_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_phone_number_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_postcode_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('postcode').max_length
        self.assertEqual(max_length, 20)

    def test_town_or_city_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('town_or_city').max_length
        self.assertEqual(max_length, 40)

    def test_street_address1_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('street_address1').max_length
        self.assertEqual(max_length, 80)

    def test_street_address2_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('street_address2').max_length
        self.assertEqual(max_length, 80)

    def test_county_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('county').max_length
        self.assertEqual(max_length, 80)

    def test_stripe_pid_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('stripe_pid').max_length
        self.assertEqual(max_length, 254)

    def test_delivery_cost_max_digits(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('delivery_cost').max_digits
        self.assertEqual(max_length, 6)

    def test_delivery_cost_decimal_places(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('delivery_cost').decimal_places
        self.assertEqual(max_length, 2)

    def test_order_total_max_digits(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_total').max_digits
        self.assertEqual(max_length, 10)

    def test_order_total_decimal_places(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_total').decimal_places
        self.assertEqual(max_length, 2)

    def test_grand_total_max_digits(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('grand_total').max_digits
        self.assertEqual(max_length, 10)

    def test_grand_total_decimal_places(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('grand_total').decimal_places
        self.assertEqual(max_length, 2)
