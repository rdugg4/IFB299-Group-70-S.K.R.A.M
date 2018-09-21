from django.test import TestCase
from django.urls import reverse

class test_createAccountView(TestCase):
    
    def test_indexHTML(self):
        response = self.client.get('/CRC/create_account/')
        self.assertTemplateUsed(response, 'testApp/ShaleenCreateYourAccountPage.html')
        
class test_customerDetailView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customers.objects.create(firstname='Kaushal', middlename='Kishorbhai', lastname='Limbasiya',
        tel = 1234567890,
        bday = 09/09/1997,
        email = 'abcd@gmail.com',
        Password = 'abcd1234')
        
    def test_Location(self):
        response = self.client.get('/CRC/create_account/')
        self.assertEqual(response.status_code, 200)