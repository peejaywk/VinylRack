from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestAppModel(TestCase):
    def setUp(self):
        # Create a user
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
        profile = UserProfile(
            user=self.user,
            default_phone_number='5551234',
            default_street_address1='12 Main Street',
            default_street_address2='Top Flat',
            default_town_or_city='York',
            default_county='Yorkshire',
            default_postcode='YH106DQ',
            default_country='UK',
        )

        expected_result = profile.user.username

        self.assertEqual(str(profile), expected_result)
