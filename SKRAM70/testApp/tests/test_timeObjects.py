from django.test import TestCase
from ..functions.timeobjects import timeObject

class test_timeObjects(TestCase):

    def test_getDate(self):
        date = 20180917
        self.assertEqual(timeObject(date).getDate(), date)
        date = 12002030
        self.assertEqual(timeObject(date).getDate(), date)
        date = 50000101
        self.assertEqual(timeObject(date).getDate(), date)
        date = 00000000
        self.assertEqual(timeObject(date).getDate(), date)

    def test_weekday(self):
        date = 20180917 # Monday
        self.assertEqual(timeObject(date).weekday(), 0)
        date = 20180911 # Tuesday
        self.assertEqual(timeObject(date).weekday(), 1)
        date = 20180919 # Wednesday
        self.assertEqual(timeObject(date).weekday(), 2)
        date = 20180906 # Thursday
        self.assertEqual(timeObject(date).weekday(), 3)
        date = 20180914 # Friday
        self.assertEqual(timeObject(date).weekday(), 4)
        date = 20180901 # Saturday
        self.assertEqual(timeObject(date).weekday(), 5)
        date = 20180930 # Sunday
        self.assertEqual(timeObject(date).weekday(), 6)

class test_timeObject(TestCase):

    def test_getDate(self):
        date = 20180917
        self.assertEqual(timeObject(date).getDate(), date)
        date = 12002030
        self.assertEqual(timeObject(date).getDate(), date)
        date = 50000101
        self.assertEqual(timeObject(date).getDate(), date)
        date = 00000000
        self.assertEqual(timeObject(date).getDate(), date)

    def test_weekday(self):
        date = 20180917 # Monday
        self.assertEqual(timeObject(date).weekday(), 0)
        date = 20180911 # Tuesday
        self.assertEqual(timeObject(date).weekday(), 1)
        date = 20180919 # Wednesday
        self.assertEqual(timeObject(date).weekday(), 2)
        date = 20180906 # Thursday
        self.assertEqual(timeObject(date).weekday(), 3)
        date = 20180914 # Friday
        self.assertEqual(timeObject(date).weekday(), 4)
        date = 20180901 # Saturday
        self.assertEqual(timeObject(date).weekday(), 5)
        date = 20180930 # Sunday
        self.assertEqual(timeObject(date).weekday(), 6)
