from django.test import TestCase
from django.urls import reverse
from testApp.models import *
from django.contrib.auth.models import User, Group
from django.contrib.messages import get_messages
from testApp.create_users.CreateTestUsers import *
from django.db.models.query import QuerySet

# Complete
class test_indexView(TestCase):
    def test_Location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'testApp/AlanaCustomerHomepageUpdated.html')

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

    def test_Context(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        resultantCars = response.context['resultantCars']
        storeList = response.context['StoreList']
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertIsInstance(storeList, QuerySet)

    def test_ContextWithGet(self):
        response = self.client.get('/search/?pickupLocation=allStores&pickupDate=2018-10-18&dropoffDate=2018-10-26&seats=5&makeOfCar=Volkswagen&carModel=Golf&bodyType=SEDAN&driveType=FWD')
        self.assertEqual(response.status_code, 200)
        resultantCars = response.context['resultantCars']
        storeList = response.context['StoreList']
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertIsInstance(storeList, QuerySet)

# Complete
class test_StaffPortalView(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    def test_NotLoggedIn(self):
        response = self.client.post('/staffPortal')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInCustomer(self):
        self.client.login(username="customer", password="1234")
        response = self.client.post('/staffPortal')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInStaff(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get('/staffPortal')
        self.assertEqual(response.status_code, 200)

    def test_LoggedInBM(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get('/staffPortal')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/MikeStaffHomePage.html')

# Complete
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
        CreateUsers()

    def test_NotLoggedInBM(self):
        response = self.client.post('/staffPortal/CarPopularity/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

        self.client.login(username="staff", password="1234")
        response = self.client.post('/staffPortal/CarPopularity/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

        self.client.login(username="customer", password="1234")
        response = self.client.post('/staffPortal/CarPopularity/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInBM(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal/CarPopularity/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal/CarPopularity/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/CarpopularityupdatedShaleen.html')

    def test_Context(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal/CarPopularity/')
        self.assertEqual(response.status_code, 200)
        graphTitle = response.context['graphTitle']
        graphType = response.context['graphType']
        counterAndNames = response.context['counterAndNames']
        self.assertIsInstance(graphTitle, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, zip)

    def test_ContextWithGet(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal/CarPopularity/?Catagory=seats&Graph=Column')
        self.assertEqual(response.status_code, 200)
        graphTitle = response.context['graphTitle']
        graphType = response.context['graphType']
        counterAndNames = response.context['counterAndNames']
        self.assertIsInstance(graphTitle, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, zip)

class test_ContactUsView(TestCase):
    def test_Location(self):
        response = self.client.post('/ContactUs')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.post('/ContactUs')
        self.assertTemplateUsed(response, 'testApp/MikeContactPage draft.html')

class test_VehicleReturnsView(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    def test_NotLoggedIn(self):
        response = self.client.post('/staffPortal/vehicleReturns/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInCustomer(self):
        self.client.login(username="customer", password="1234")
        response = self.client.post('/staffPortal/vehicleReturns/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInStaff(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get('/staffPortal/vehicleReturns/')
        self.assertEqual(response.status_code, 200)

    def test_LoggedInBM(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal/vehicleReturns/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get('/staffPortal/vehicleReturns/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/CarReturnsUpdatedShaleen.html')

    def test_Context(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal/vehicleReturns/')
        self.assertEqual(response.status_code, 200)
        graphTitle = response.context['graphTitle']
        graphType = response.context['graphType']
        counterAndNames = response.context['counterAndNames']
        storeList = response.context['StoreList']
        zippedResults = response.context['zippedResults']
        startDate = response.context['startDate']
        storeIDformatted = response.context['storeIDformatted']
        self.assertIsInstance(storeList, QuerySet)
        self.assertIsInstance(graphTitle, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, zip)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)

    def test_ContextWithGet(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/staffPortal/vehicleReturns/?ordering=weekly&start_date=&returnStore=allStores&Graph=None')
        self.assertEqual(response.status_code, 200)
        graphTitle = response.context['graphTitle']
        graphType = response.context['graphType']
        counterAndNames = response.context['counterAndNames']
        storeList = response.context['StoreList']
        zippedResults = response.context['zippedResults']
        startDate = response.context['startDate']
        storeIDformatted = response.context['storeIDformatted']
        self.assertIsInstance(storeList, QuerySet)
        self.assertIsInstance(graphTitle, str)
        self.assertIsInstance(graphType, str)
        self.assertIsInstance(counterAndNames, zip)
        self.assertIsInstance(zippedResults, list)
        self.assertIsInstance(startDate, str)
        self.assertIsInstance(storeIDformatted, str)


class test_SuccessfulLogin(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    def test_LoggedInStaff(self):
        self.client.login(username="staff", password="1234")
        response = self.client.post('/successfulLogin')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Login successful')
        self.assertRedirects(response, '/staffPortal', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInBM(self):
        self.client.login(username="BM", password="1234")
        response = self.client.post('/successfulLogin')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Login successful')
        self.assertRedirects(response, '/staffPortal', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInCustomer(self):
        self.client.login(username="customer", password="1234")
        response = self.client.post('/successfulLogin')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Login successful')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

class test_LocationsView(TestCase):
    def test_Location(self):
        response = self.client.post('/Locations')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        response = self.client.post('/Locations')
        self.assertTemplateUsed(response, 'testApp/LocationsPage.html')

    # This section needs to be done
    # def test_context(self):

class test_CarRecomView(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    def test_NotLoggedInCustomer(self):
        response = self.client.post('/RecommendCars')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

        self.client.login(username="staff", password="1234")
        response = self.client.post('/RecommendCars')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

        self.client.login(username="BM", password="1234")
        response = self.client.post('/RecommendCars')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You MUST be logged in to access that page')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInCustomer(self):
        self.client.login(username="customer", password="1234")
        response = self.client.get('/RecommendCars')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        self.client.login(username="customer", password="1234")
        response = self.client.get('/RecommendCars')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/ShaleenSearchresults.html')

    def test_Context(self):
        self.client.login(username="customer", password="1234")
        response = self.client.get('/RecommendCars')
        self.assertEqual(response.status_code, 200)
        resultantCars = response.context['resultantCars']
        storeList = response.context['StoreList']
        self.assertIsInstance(resultantCars, QuerySet)
        self.assertIsInstance(storeList, QuerySet)


## KAUSHAL'S TEST CASES TO DO
class test_EditCustomersView(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()

    def test_LoggedOut(self):
        response = self.client.post('/editUser/')
        self.assertRedirects(response, '/accounts/login/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_LoggedInAsCustomer(self):
        self.client.login(username="customer", password="1234")
        response = self.client.get('/editUser/')
        self.assertEqual(response.status_code, 200)

    def test_Context(self):
        self.client.login(username="customer", password="1234")
        response = self.client.get('/editUser/')
        self.assertEqual(response.status_code, 200)
        customer = response.context['customer']
        dob = response.context['dob']
        self.assertIsInstance(customer, Customers)
        self.assertIsInstance(dob, str)


    def test_LoggedInAsBM(self):
        self.client.login(username="BM", password="1234")
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)


    def test_LoggedInAsStaff(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)


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

class test_CreateAccountView(TestCase):
    @classmethod
    def setUpTestData(cls):
        CreateUsers()
    

    def test_LoggedInAsCustomer(self):
        self.client.login(username="customer", password="1234")
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_LoggedOut(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_Template(self):
        # self.client.login(username="customer", password="1234")
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testApp/login.html')