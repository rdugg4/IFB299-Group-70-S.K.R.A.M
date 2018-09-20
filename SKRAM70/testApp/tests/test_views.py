from django.test import TestCase
from django.urls import reverse

class test_indexView(TestCase):

    def test_indexLocation(self):
        response = self.client.get('/CRC/')
        self.assertEqual(response.status_code, 200)

    def test_indexHTML(self):
        response = self.client.get('/CRC/')
        self.assertTemplateUsed(response, 'testApp/AlanaCustomerHomepage.html')
