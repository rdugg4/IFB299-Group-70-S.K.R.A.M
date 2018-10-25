from django.test import TestCase
from django.test.client import RequestFactory
from testApp.create_users.CreateTestUsers import *
from testApp.create_users.create_testing_data import *
from django.contrib.auth.models import User, Group, AnonymousUser
from ..functions.search import *
from django.db.models.query import QuerySet
from testApp.models import *

class test_RecommendCars(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()
        CreateTestData()

    def setUp(self):
        self.factory = RequestFactory()

    def test_User1(self):
        request = self.factory.get('/')
        request.user = User.objects.get(username='customer')
        resultantCars = carSets.reccomendCars(request)
        self.assertIsInstance(resultantCars, QuerySet)
        # for car in resultantCars:
        #     self.assertIsInstance(resultantCars, QuerySet)

class test_SearchCars(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()
        CreateTestData()

    def setUp(self):
        self.factory = RequestFactory()

    def test_NonDefinedInputs(self):
        request = self.factory.get('/')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)

    def test_DateInputs(self):
        request = self.factory.get('/search/?pickupDate=2019-10-18&dropoffDate=2019-10-26')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 20)

        request = self.factory.get('/search/?pickupDate=2018-10-18&dropoffDate=2018-10-26')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 13)

        request = self.factory.get('/search/?pickupDate=2018-06-18&dropoffDate=2018-06-26')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 18)

    def test_StoreInputs(self):
        requests = []
        for store in Stores.objects.all():
            urlString = '/search/?pickupLocation=' + str(store.id)
            requests.append(self.factory.get(urlString))
        resultantCars = carSets.searchData(requests[len(requests) - 2])
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 9)

        resultantCars = carSets.searchData(requests[len(requests) - 1])
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 4)

    # Car only related inputs
    def test_SeatInputs(self):
        request = self.factory.get('/search/?seats=5&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 15)

        request = self.factory.get('/search/?seats=4&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 4)

        request = self.factory.get('/search/?seats=7&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 1)

        request = self.factory.get('/search/?seats=3&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 0)

        request = self.factory.get('/search/?seats=6&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 0)

        request = self.factory.get('/search/?seats=8&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 0)

    def test_MakeOfCarInputs(self):
        request = self.factory.get('/search/?makeOfCar=Volkswagen&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 2)

        request = self.factory.get('/search/?makeOfCar=BMW&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 3)

        request = self.factory.get('/search/?makeOfCar=NISSAN&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 2)

    def test_CarModelInputs(self):
        request = self.factory.get('/search/?carModel=Golf&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 2)

        request = self.factory.get('/search/?carModel=200&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 2)

        request = self.factory.get('/search/?carModel=ML&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 1)

    def test_BodyTypeInputs(self):
        request = self.factory.get('/search/?bodyType=SEDAN&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 6)

        request = self.factory.get('/search/?bodyType=HATCHBACK&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 4)

        request = self.factory.get('/search/?bodyType=CABRIOLET&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 2)

        request = self.factory.get('/search/?bodyType=WAGON&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 5)

    def test_DriveTypeInputs(self):
        request = self.factory.get('/search/?driveType=FWD&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 7)

        request = self.factory.get('/search/?driveType=RWD&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 7)

        request = self.factory.get('/search/?driveType=4WD&pickupDate=2020-10-18')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 4)

    def test_fullyDefinedInputs(self):
        request = self.factory.get('/search/?pickupLocation=allStores&pickupDate=2019-10-18&dropoffDate=2019-10-26&seats=5&makeOfCar=Volkswagen&carModel=Golf&bodyType=5D HATCHBACK&driveType=FWD')
        resultantCars = carSets.searchData(request)
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertEqual(resultantCars.count(), 2)
