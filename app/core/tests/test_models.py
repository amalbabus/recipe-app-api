from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_an_email_is_successful(self):
        email = 'amalbabus33@gmail.com'
        password ='testpass123'

        user =get_user_model().objects.create_user(email= email, password=password)


        self.assertEquals(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_valid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password=password')

