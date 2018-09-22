from django.test import TestCase
from testApp.models import *

class test_StoresModel(TestCase):

    def test_Labels(self):
        field_label = Stores._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        field_label = Stores._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')
        field_label = Stores._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')
        field_label = Stores._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')
        field_label = Stores._meta.get_field('state').verbose_name
        self.assertEquals(field_label, 'state')

    def test_FieldLengths(self):
        max_length = Stores._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
        max_length = Stores._meta.get_field('address').max_length
        self.assertEquals(max_length, 255)
        max_length = Stores._meta.get_field('phone').max_length
        self.assertEquals(max_length, 20)
        max_length = Stores._meta.get_field('city').max_length
        self.assertEquals(max_length, 255)
        max_length = Stores._meta.get_field('state').max_length
        self.assertEquals(max_length, 255)

class test_CarsModel(TestCase):

    def test_Labels(self):
        field_label = Cars._meta.get_field('car_makename').verbose_name
        self.assertEquals(field_label, 'car makename')
        field_label = Cars._meta.get_field('car_model').verbose_name
        self.assertEquals(field_label, 'car model')
        field_label = Cars._meta.get_field('car_series').verbose_name
        self.assertEquals(field_label, 'car series')
        field_label = Cars._meta.get_field('car_seriesyear').verbose_name
        self.assertEquals(field_label, 'car seriesyear')
        field_label = Cars._meta.get_field('car_pricenew').verbose_name
        self.assertEquals(field_label, 'car pricenew')
        field_label = Cars._meta.get_field('car_enginesize').verbose_name
        self.assertEquals(field_label, 'car enginesize')
        field_label = Cars._meta.get_field('car_fuelsystem').verbose_name
        self.assertEquals(field_label, 'car fuelsystem')
        field_label = Cars._meta.get_field('car_tankcapacity').verbose_name
        self.assertEquals(field_label, 'car tankcapacity')
        field_label = Cars._meta.get_field('car_power').verbose_name
        self.assertEquals(field_label, 'car power')
        field_label = Cars._meta.get_field('car_seatingcapacity').verbose_name
        self.assertEquals(field_label, 'car seatingcapacity')
        field_label = Cars._meta.get_field('car_standardtransmission').verbose_name
        self.assertEquals(field_label, 'car standardtransmission')
        field_label = Cars._meta.get_field('car_bodytype').verbose_name
        self.assertEquals(field_label, 'car bodytype')
        field_label = Cars._meta.get_field('car_drive').verbose_name
        self.assertEquals(field_label, 'car drive')
        field_label = Cars._meta.get_field('car_wheelbase').verbose_name
        self.assertEquals(field_label, 'car wheelbase')

    def test_FieldLengths(self):
        max_length = Cars._meta.get_field('car_makename').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_model').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_series').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_enginesize').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_fuelsystem').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_tankcapacity').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_power').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_standardtransmission').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_bodytype').max_length
        self.assertEquals(max_length, 255)
        max_length = Cars._meta.get_field('car_drive').max_length
        self.assertEquals(max_length, 3)
        max_length = Cars._meta.get_field('car_wheelbase').max_length
        self.assertEquals(max_length, 255)

class test_CustomersModel(TestCase):

    def test_Labels(self):
        field_label = Customers._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        field_label = Customers._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')
        field_label = Customers._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')
        field_label = Customers._meta.get_field('dob').verbose_name
        self.assertEquals(field_label, 'dob')
        field_label = Customers._meta.get_field('occupation').verbose_name
        self.assertEquals(field_label, 'occupation')
        field_label = Customers._meta.get_field('gender').verbose_name
        self.assertEquals(field_label, 'gender')
        field_label = Customers._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')
        field_label = Customers._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_FieldLengths(self):
        max_length = Customers._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
        max_length = Customers._meta.get_field('phone').max_length
        self.assertEquals(max_length, 20)
        max_length = Customers._meta.get_field('address').max_length
        self.assertEquals(max_length, 255)
        max_length = Customers._meta.get_field('dob').max_length
        self.assertEquals(max_length, 20)
        max_length = Customers._meta.get_field('occupation').max_length
        self.assertEquals(max_length, 255)
        max_length = Customers._meta.get_field('gender').max_length
        self.assertEquals(max_length, 3)
        max_length = Customers._meta.get_field('email').max_length
        self.assertEquals(max_length, 255)
        max_length = Customers._meta.get_field('password').max_length
        self.assertEquals(max_length, 255)
