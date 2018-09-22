from django.test import TestCase
from django.urls import reverse

class test_createAccountView(TestCase):
    
    def test_indexHTML(self):
        response = self.client.get('/CRC/create_accounts/')
        self.assertTemplateUsed(response, 'testApp/ShaleenCreateYourAccountPage.html')