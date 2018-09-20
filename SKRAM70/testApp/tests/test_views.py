from django.test import TestCase
from django.urls import reverse
from testApp.models import *

class test_indexView(TestCase):

    def test_Location(self):
        response = self.client.get('/CRC/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/CRC/')
        self.assertTemplateUsed(response, 'testApp/AlanaCustomerHomepage.html')

class test_carDetailView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cars.objects.create(car_makename='make BMW', car_model='model x3', car_series='Series',
        car_seriesyear = 2006,
        car_pricenew = 5000,
        car_enginesize = 'Big',
        car_fuelsystem = 'deisel',
        car_tankcapacity = '4L',
        car_power = 'Lots',
        car_seatingcapacity = 6,
        car_standardtransmission = 'Standardtransmission',
        car_bodytype = 'hatchback',
        car_drive = '4WD',
        car_wheelbase = '4000mm')

    def test_Location(self):
        response = self.client.get('/CRC/1/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/CRC/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/showcaroriginal.html')

    def test_Context(self):
        carDBs = Cars.objects.filter(id=1)
        response = self.client.get('/CRC/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('CarInfo' in response.context)
        self.assertEqual(response.context['CarInfo'].count(), 1)
        for car in response.context['CarInfo']:
            for carDB in carDBs:
                self.assertEqual(car.id, carDB.id)

class test_searchResults(TestCase):
    @classmethod
    def setUpTestData(cls):
        numOfResults = 20
        for carid in range(numOfResults):
            Cars.objects.create(car_makename='make {carid}',
            car_model='model {carid}',
            car_series='Series {carid}',
            car_seriesyear = 2006,
            car_pricenew = 5000,
            car_enginesize = 'eiginesize {carid}',
            car_fuelsystem = 'fuelsystem {carid}',
            car_tankcapacity = 'tankcapacity {carid}',
            car_power = 'power {carid}',
            car_seatingcapacity = carid,
            car_standardtransmission = 'Standardtransmission {carid}',
            car_bodytype = 'hatchback {carid}',
            car_drive = '4WD',
            car_wheelbase = '4000mm {carid}')

    def test_Location(self):
        response = self.client.get('/CRC/search/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/CRC/search/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/ShaleenSearchresults.html')

    # def test_Context(self):
    #     carDBs = Cars.objects.filter(id=1)
    #     response = self.client.get('/CRC/1/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('CarInfo' in response.context)
    #     self.assertEqual(response.context['CarInfo'].count(), 1)
    #     for car in response.context['CarInfo']:
    #         for carDB in carDBs:
    #             self.assertEqual(car.id, carDB.id)
