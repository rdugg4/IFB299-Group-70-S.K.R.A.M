from django.test import TestCase
from django.test.client import RequestFactory
from ..functions.userVerification import *
from testApp.create_users.CreateTestUsers import *

class test_UserVerification(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    # def setUpRequests(self):


    def test_LoggedIn(self):
        self.factory = RequestFactory()
        # request = self.factory.get('/')
        # self.assertFalse(UserVerification.LoggedIn(request))
        # self.client.login(username="customer", password="1234")
