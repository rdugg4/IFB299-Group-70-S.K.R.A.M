from django.test import TestCase
from django.test.client import RequestFactory
from testApp.create_users.CreateTestUsers import *
from testApp.create_users.create_testing_data import *
from django.contrib.auth.models import User, Group, AnonymousUser
from ..functions.vehicleReturns import *
from django.db.models.query import QuerySet
from testApp.models import *

class test_VehicleReturns(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()
        CreateTestData()

    def setUp(self):
        self.factory = RequestFactory()

    def test_NoInputs(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)

        self.assertEqual(lengthOfGrouping, "Week")
        self.assertEqual(graphType, "None")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

        counterAndNames = list(counterAndNames)
        self.assertEqual(len(counterAndNames), 1)
        self.assertEqual(counterAndNames[0][0], 2)
        self.assertEqual(counterAndNames[0][1], 'Week 1')

        zippedResults = list(zippedResults[0])
        self.assertEqual(len(zippedResults), 2)
        self.assertTrue(zippedResults[0][0].returndate >= 20181025)
        self.assertTrue(zippedResults[1][0].returndate >= 20181025)

        self.assertEqual(zippedResults[0][0].carid, zippedResults[0][1])
        self.assertEqual(zippedResults[0][0].customerid, zippedResults[0][2])
        self.assertEqual(zippedResults[0][0].returnstore, zippedResults[0][3])
        self.assertEqual(zippedResults[1][0].carid, zippedResults[1][1])
        self.assertEqual(zippedResults[1][0].customerid, zippedResults[1][2])
        self.assertEqual(zippedResults[1][0].returnstore, zippedResults[1][3])

    def test_GraphTypeInputs(self):
        request = self.factory.get('/?Graph=None')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)

        self.assertEqual(lengthOfGrouping, "Week")
        self.assertEqual(graphType, "None")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

        request = self.factory.get('/?Graph=Column')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)

        self.assertEqual(lengthOfGrouping, "Week")
        self.assertEqual(graphType, "Column")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

        request = self.factory.get('/?Graph=Pie')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)

        self.assertEqual(lengthOfGrouping, "Week")
        self.assertEqual(graphType, "Pie")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

    def test_LengthInputs(self):
        request = self.factory.get('/?ordering=weekly')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)
        self.assertEqual(lengthOfGrouping, "Week")
        self.assertEqual(graphType, "None")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

        request = self.factory.get('/?ordering=daily')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)
        self.assertEqual(lengthOfGrouping, "Day")
        self.assertEqual(graphType, "None")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

        request = self.factory.get('/?ordering=monthly')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)
        self.assertEqual(lengthOfGrouping, "Month")
        self.assertEqual(graphType, "None")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

    def test_StoreInputs(self):
        request = self.factory.get('/?ordering=monthly')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)
        self.assertEqual(lengthOfGrouping, "Month")
        self.assertEqual(graphType, "None")
        self.assertEqual(startDate, "")
        self.assertEqual(storeIDformatted, "")

    def test_DateInputs(self):
        request = self.factory.get('/?returndate=2000-10-18')
        request.user = AnonymousUser()
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        self.assertIsInstance(lengthOfGrouping, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, list)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)

        counterAndNames = list(counterAndNames)
        self.assertEqual(len(counterAndNames), 1)
        self.assertEqual(counterAndNames[0][0], 2)
        self.assertEqual(counterAndNames[0][1], 'Week 1')

        zippedResults = list(zippedResults[0])
        self.assertEqual(len(zippedResults), 2)
        for groupResults in zippedResults:
            self.assertTrue(groupResults[0].returndate >= 20001025)
            self.assertEqual(groupResults[0].carid, groupResults[1])
            self.assertEqual(groupResults[0].customerid, groupResults[2])
            self.assertEqual(groupResults[0].returnstore, groupResults[3])

    # def test_loggedInAsStaff(self):
