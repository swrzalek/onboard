from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='sample@user.pl', password='testpassword'):
    # Crreate sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_premises(
    name='Szot',
    image_url='https://via.placeholder.com/350x150',
    city='Gdynia'
):
    return models.Premises.objects.create(name=name, image_url=image_url, city=city)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is succesful"""
        email = 'test@test.com'
        password = 'testpassowrd123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Terst the email for a new user is normalized"""
        email = 'sample@SAMPLE.test'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_empty_user_raises_error(self):
        """Test that no username raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.pl',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_new_superuser_with_name(self):
        """Test to create user with name"""
        email = 'test@test.com'
        password = 'testpassowrd123'
        name = 'Mike'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name,
        )
        self.assertEqual(user.name, name)

    def test_premises_str(self):
        """Test the premises string represent"""
        premises = models.Premises.objects.create(
            name='Szot',
            image_url='https://via.placeholder.com/350x150',
            city='Gdynia',
        )

        self.assertEqual(str(premises), premises.name)

    def test_orders_str(self):
        """Test orders string represent"""

        order = models.Order.objects.create(
            status="REQUESTED",
            premises=sample_premises()
        )
        self.assertEqual(str(order), str(order.id))
