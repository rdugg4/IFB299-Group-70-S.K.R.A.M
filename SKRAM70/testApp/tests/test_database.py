from django.test import TestCase
from django.urls import reverse
from testApp.models import Customers
# from .models import Customers
import datetime

class test_createAccountView(TestCase):

    def test_indexHTML(self):
        response = self.client.get('/CRC/create_account/')
        self.assertTemplateUsed(response, 'testApp/ShaleenCreateYourAccountPage.html')

class test_customerDetailView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customers.objects.create(name='Kaushal Kishorbhai Limbasiya',
        phone = 1234567890,
        dob = 19970909,
        email = 'abcd@gmail.com',
        password = 'abcd1234')

    def test_Location(self):
        response = self.client.post('/CRC/create_account/')
        self.assertEqual(response.status_code, 200)

        