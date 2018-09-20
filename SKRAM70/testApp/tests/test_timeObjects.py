from django.test import TestCase
from ..functions.timeobjects import *

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

class test_givenTime(TestCase):

    def test_givenTimeCreationYMD(self):
        inputtedDate = '2018-09-17'
        date = 20180917
        self.assertEqual(givenTime(inputtedDate, "YMD").getDate(), date)
        inputtedDate = '1200F20930'
        date = 12002030
        self.assertEqual(givenTime(inputtedDate, "YMD").getDate(), date)
        inputtedDate = '5000101W01'
        date = 50000101
        self.assertEqual(givenTime(inputtedDate, "YMD").getDate(), date)
        inputtedDate = '0000X00P00'
        date = 00000000
        self.assertEqual(givenTime(inputtedDate, "YMD").getDate(), date)

    def test_givenTimeCreationDMY(self):
        inputtedDate = '17-09-2018'
        date = 20180917
        self.assertEqual(givenTime(inputtedDate, "DMY").getDate(), date)
        inputtedDate = '30F2091200'
        date = 12002030
        self.assertEqual(givenTime(inputtedDate, "DMY").getDate(), date)
        inputtedDate = '01101W5000'
        date = 50000101
        self.assertEqual(givenTime(inputtedDate, "DMY").getDate(), date)
        inputtedDate = '00X00P0000'
        date = 00000000
        self.assertEqual(givenTime(inputtedDate, "DMY").getDate(), date)
