from django.test import TestCase
from django.test.client import RequestFactory
from ..functions.inputVerification import *
from testApp.create_users.CreateTestUsers import *
from django.contrib.auth.models import User, Group, AnonymousUser

class test_UserVerification(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    def setUp(self):
        self.factory = RequestFactory()

    def test_isint(self):
        request = self.factory.get('/search/?seats=5')
        inputVeriObj = inputVerification(request)
        self.assertTrue(inputVeriObj.isint(10))
        self.assertTrue(inputVeriObj.isint('10'))
        self.assertFalse(inputVeriObj.isint('failure'))
        self.assertFalse(inputVeriObj.isint('10.01'))

    def test_isdate(self):
        request = self.factory.get('/search/?pickupLocation=allStores&pickupDate=2018-10-18&dropoffDate=2018-10-26&seats=5&makeOfCar=Volkswagen')
        inputVeriObj = inputVerification(request)
        self.assertTrue(inputVeriObj.isdate('pickupDate'))
        self.assertTrue(inputVeriObj.isdate('dropoffDate'))
        self.assertFalse(inputVeriObj.isdate('pickupLocation'))
        self.assertFalse(inputVeriObj.isdate('seats'))

    def test_checkExistance(self):
        request = self.factory.get('/search/?pickupLocation=allStores&pickupDate=2018-10-18&dropoffDate=2018-10-26&seats=5&makeOfCar=Volkswagen')
        inputVeriObj = inputVerification(request)
        self.assertTrue(inputVeriObj.checkExistance('pickupDate'))
        self.assertTrue(inputVeriObj.checkExistance('dropoffDate'))
        self.assertTrue(inputVeriObj.checkExistance('pickupLocation'))
        self.assertTrue(inputVeriObj.checkExistance('seats'))
        self.assertFalse(inputVeriObj.checkExistance('failure'))

    def test_checkFormGET(self):
        request = self.factory.get('/search/?pickupLocation=allStores&pickupDate=2018-10-18&dropoffDate=2018-10-26&seats=5&makeOfCar=Volkswagen')
        inputVeriObj = inputVerification(request)
        self.assertTrue(inputVeriObj.checkFormGET('pickupDate', 'date'))
        self.assertTrue(inputVeriObj.checkFormGET('dropoffDate', 'date'))
        self.assertFalse(inputVeriObj.checkFormGET('pickupDate', 'num'))
        self.assertFalse(inputVeriObj.checkFormGET('dropoffDate', 'num'))
        self.assertTrue(inputVeriObj.checkFormGET('pickupLocation', 'test'))
        self.assertFalse(inputVeriObj.checkFormGET('pickupLocation', 'date'))
        self.assertFalse(inputVeriObj.checkFormGET('pickupLocation', 'num'))
        self.assertTrue(inputVeriObj.checkFormGET('seats', 'num'))
        self.assertTrue(inputVeriObj.checkFormGET('seats', 'test'))
