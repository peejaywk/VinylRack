from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestAppModel(TestCase):
    def setUp(self):
        # Create a user - this will also create a user profile.
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com'
        )
        self.user.set_password('!password1234!')
        self.user.save()

    def test_profile_str(self):
        """
        Test to check the correct string is returned by the __str__
        method in the UserProfile model
        """
        profile = UserProfile.objects.get(id=1)
        expected_result = profile.user.username

        self.assertEqual(str(profile), expected_result)

    # Check that the values of the field labels are correct
    def test_default_phone_number_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_phone_number').verbose_name
        self.assertEqual(field_label, 'default phone number')

    def test_default_street_address1_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_street_address1').verbose_name
        self.assertEqual(field_label, 'default street address1')

    def test_default_street_address2_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_street_address2').verbose_name
        self.assertEqual(field_label, 'default street address2')

    def test_default_town_or_city_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_town_or_city').verbose_name
        self.assertEqual(field_label, 'default town or city')

    def test_default_county_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_county').verbose_name
        self.assertEqual(field_label, 'default county')

    def test_default_postcode_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_postcode').verbose_name
        self.assertEqual(field_label, 'default postcode')

    def test_default_country_label(self):
        profile = UserProfile.objects.get(id=1)
        field_label = profile._meta.get_field('default_country').verbose_name
        self.assertEqual(field_label, 'default country')

    # Check that the size of the character fields are correct.
    def test_default_phone_number_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_default_street_address1_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_street_address1').max_length
        self.assertEqual(max_length, 80)

    def test_default_street_address2_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_street_address2').max_length
        self.assertEqual(max_length, 80)

    def test_default_town_or_city_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_town_or_city').max_length
        self.assertEqual(max_length, 40)

    def test_default_county_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_county').max_length
        self.assertEqual(max_length, 80)

    def test_default_postcode_max_length(self):
        profile = UserProfile.objects.get(id=1)
        max_length = profile._meta.get_field('default_postcode').max_length
        self.assertEqual(max_length, 20)