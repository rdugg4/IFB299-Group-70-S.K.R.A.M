from django.test import TestCase
from django.test.client import RequestFactory
from ..functions.userVerification import *
from testApp.create_users.CreateTestUsers import *
from django.contrib.auth.models import User, Group, AnonymousUser

class test_UserVerification(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    def setUp(self):
        self.factory = RequestFactory()

    def test_LoggedIn(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        self.assertFalse(UserVerification.LoggedIn(request))

        request.user = User.objects.get(username='customer')
        self.assertTrue(UserVerification.LoggedIn(request))

        request.user = User.objects.get(username='staff')
        self.assertTrue(UserVerification.LoggedIn(request))

        request.user = User.objects.get(username='BM')
        self.assertTrue(UserVerification.LoggedIn(request))

    def test_CustomerLoggedIn(self):
        request = self.factory.get('/')

        request.user = AnonymousUser()
        self.assertFalse(UserVerification.CustomerLoggedIn(request))

        request.user = User.objects.get(username='customer')
        self.assertTrue(UserVerification.CustomerLoggedIn(request))

        request.user = User.objects.get(username='staff')
        self.assertFalse(UserVerification.CustomerLoggedIn(request))

        request.user = User.objects.get(username='BM')
        self.assertFalse(UserVerification.CustomerLoggedIn(request))

    def test_BoardMemberLoggedIn(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        self.assertFalse(UserVerification.BoardMemberLoggedIn(request))

        request.user = User.objects.get(username='customer')
        self.assertFalse(UserVerification.BoardMemberLoggedIn(request))

        request.user = User.objects.get(username='staff')
        self.assertFalse(UserVerification.BoardMemberLoggedIn(request))

        request.user = User.objects.get(username='BM')
        self.assertTrue(UserVerification.BoardMemberLoggedIn(request))

    def test_StaffLoggedIn(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        self.assertFalse(UserVerification.StaffLoggedIn(request))

        request.user = User.objects.get(username='customer')
        self.assertFalse(UserVerification.StaffLoggedIn(request))

        request.user = User.objects.get(username='staff')
        self.assertTrue(UserVerification.StaffLoggedIn(request))

        request.user = User.objects.get(username='BM')
        self.assertTrue(UserVerification.StaffLoggedIn(request))
