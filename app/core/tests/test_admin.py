from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        # self.adminuser = get_user_model().objects.create_superuser( email= "amalbabus44@gmail.com", 
        #                                                             password="rtesfs")

        # self.client.force_login(self.adminuser)
        self.user = get_user_model().objects.create_user( email= "amalbabus44@gmail.com", 
                                                                    password="rtesfs", name="amal ba")

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response,self.user.name)
        self.assertContains(response,self.user.email)

        
