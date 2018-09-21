from django.test import TestCase
from ..functions.timeobjects import *

from unittest import mock
import datetime

# test timeObject class
class test_timeObject(TestCase):
    # test the getDate function for timeObject
    def test_getDate(self):
        date = 20180917
        self.assertEqual(timeObject(date).getDate(), date)
        date = 12002030
        self.assertEqual(timeObject(date).getDate(), date)
        date = 50000101
        self.assertEqual(timeObject(date).getDate(), date)
        date = 00000000
        self.assertEqual(timeObject(date).getDate(), date)

    # test the weekday function for timeObject
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

# test givenTime object
class test_givenTime(TestCase):
    # test the creation of the givenTime object with YMD type
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

    # test the creation of the givenTime object with DMY type
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

class test_currentTime(TestCase):

    def test_currentTimeCreation(self):
        with mock.patch('datetime.datetime') as dt_mock:
            dt_mock.now.return_value.strftime.return_value = '20060204'
            date = 20060204
            self.assertEqual(currentTime().getDate(), date)

            dt_mock.now.return_value.strftime.return_value = '30061201'
            date = 30061201
            self.assertEqual(currentTime().getDate(), date)

            dt_mock.now.return_value.strftime.return_value = '23060131'
            date = 23060131
            self.assertEqual(currentTime().getDate(), date)

            dt_mock.now.return_value.strftime.return_value = '20180917'
            date = 20180917
            self.assertEqual(currentTime().getDate(), date)
