from django.test import TestCase
from django.urls import reverse
from testApp.models import *
from django.contrib.auth.models import User, Group
from django.contrib.messages import get_messages

class test_indexView(TestCase):

    def test_Location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/')
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
        response = self.client.get('/CarInfo/1/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/CarInfo/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/showcaroriginal.html')

    def test_Context(self):
        carDB = Cars.objects.get(id=1)
        response = self.client.get('/CarInfo/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('CarInfo' in response.context)
        self.assertEqual(response.context['CarInfo'].count(), 1)
        for car in response.context['CarInfo']:
            self.assertEqual(car.id, carDB.id)

class test_searchResultsView(TestCase):
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
            car_seatingcapacity = 6,
            car_standardtransmission = 'Standardtransmission {carid}',
            car_bodytype = 'hatchback {carid}',
            car_drive = '4WD',
            car_wheelbase = '4000mm {carid}')

    def test_Location(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/ShaleenSearchresults.html')


class test_StaffPortalView(TestCase):
    @classmethod
    def setUpTestData(cls):
        staffUser = User.objects.create_user('testStaff', 'test@email.com', 'testStaff')
        staff_group, created = Group.objects.get_or_create(name='staff_group')
        staff_group.user_set.add(staffUser)

        Stores.objects.create(name = "testName",
            address = "testAdress",
            phone = "045555555",
            city = "testCity",
            state = "testState")

        for storeObject in Stores.objects.all():
            StaffMembers.objects.create(user=staffUser, storeid=storeObject)

        BMUser = User.objects.create_user('testBM', 'test@email.com', 'testBM')
        boardMember_group, created = Group.objects.get_or_create(name='boardMember_group')
        boardMember_group.user_set.add(BMUser)

    def test_NotLoggedIn(self):
        response = self.client.post('/staffPortal')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInCustomer(self):
        response = self.client.post('/staffPortal')

    def test_LoggedInStaff(self):
        self.client.login(username="testStaff", password="testStaff")
        response = self.client.get('/staffPortal')
        self.assertEqual(response.status_code, 200)

    def test_LoggedInBM(self):
        self.client.login(username="testBM", password="testBM")
        response = self.client.get('/staffPortal')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        self.client.login(username="testStaff", password="testStaff")
        response = self.client.get('/staffPortal')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/MikeStaffHomePage.html')

class test_FAQView(TestCase):
    def test_Location(self):
        response = self.client.get('/FrequentlyAskedQuestions')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/FrequentlyAskedQuestions')
        self.assertTemplateUsed(response, 'testApp/FAQpage.html')

class test_CarPopularityView(TestCase):
    @classmethod
    def setUpTestData(cls):
        BMUser = User.objects.create_user('testBM', 'test@email.com', 'testBM')
        boardMember_group, created = Group.objects.get_or_create(name='boardMember_group')
        boardMember_group.user_set.add(BMUser)

    def test_NotLoggedIn(self):
        response = self.client.post('/staffPortal/CarPopularity/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInBM(self):
        self.client.login(username="testBM", password="testBM")
        response = self.client.get('/staffPortal/CarPopularity/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        self.client.login(username="testBM", password="testBM")
        response = self.client.get('/staffPortal/CarPopularity/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/testCarpopularity.html')

class test_EditCustomersView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customers.objects.create(name='Kaushal Kishorbhai Limbasiya',
        phone = 1234567890,
        dob = 19970909,
        email = 'abcd@gmail.com',
        password = 'abcd1234')

        customerUser = User.objects.create_user(username = 'customer', email = 'test@email.com', password = 'customer')
        customer_group, created = Group.objects.get_or_create(name = 'customer_group')
        customer_group.user_set.add(customerUser)

        for customerObject in Customers.objects.all():
            Profile.objects.create(user = customerUser, customerid = customerObject)



    def test_LoggedOut(self):
        response = self.client.post('/editUser')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInAsCustomer(self):
        self.client.login(username="customer", password="customer")
        response = self.client.post('/editUser')
        self.assertEqual(response.status_code, 200)
        