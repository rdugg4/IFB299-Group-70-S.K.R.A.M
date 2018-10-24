from ..models import *

def CreateTestData():
    # Any values such as car_model='model' are string based inputs and require
    # '' around the inputs. Values such as car_seriesyear = 2006 require integer
    # inputs (numbers without decimal places). I have given and example of each
    # kind of Object I want created, with details about how many and with what
    # inputs

    # This defines an object of the cars type. I would like 20 cars. I would
    # like some of the cars to have similar information, for instance, a couple
    # of cars should have the same makename, and a couple of cars should have
    # the same drive type.
    # Special consideration, car_drive string length cannot be longer than 3
    # I would recommend values such as 4WD, RWD, FWD


    # Finally Orders. I will need 20-30. Orders is the part that is a bit more complex.
    # This complextity comes from the fact that the inputs into the pickupstore,
    # returnstore, customerid and carid columns need to be previously created
    # store, customer and car objects respectively. For this reason I have given
    # a couple of examples.
    # As for the inputs, please make a 5-10 have a return date in the future.
    # Some have both start and return date in the past
    # Have the same cars hired a few times
    # Have a variety of customers hire cars
    # Dates of format YYYYMMDD
    order1 = Orders(createdate = 20180703,
        pickupdate = 20180704,
        pickupstore = store1,
        returndate = 20180820,
        returnstore = store1,
        droppedoff = 'TRUE',
        customerid = customer1,
        carid = car1)
    order1.save()

    order2 = Orders(createdate = 20180703,
        pickupdate = 20180704,
        pickupstore = store2,
        returndate = 20180820,
        returnstore = store1,
        droppedoff = 'FALSE',
        customerid = customer1,
        carid = car2)
    order2.save()

    order3 = Orders(createdate = 20181018,
        pickupdate = 20181020,
        pickupstore = store17,
        returndate = 20181103,
        returnstore = store17,
        droppedoff = 'FALSE',
        customerid = 11015,
        carid = 14838)
    order3.save()

    order4 = Orders(createdate = 20180101,
        pickupdate = 20180101,
        pickupstore = store3,
        returndate = 20180901,
        returnstore = store12,
        droppedoff = 'TRUE',
        customerid = 11051,
        carid = 14871)
    order4.save()

    order5 = Orders(createdate = 20180201,
        pickupdate = 20180214,
        pickupstore = store21,
        returndate = 20180217,
        returnstore = store22,
        droppedoff = 'TRUE',
        customerid = 11313,
        carid = 15127)
    order5.save()

    order6 = Orders(createdate = 20180217,
        pickupdate = 20180221,
        pickupstore = store40,
        returndate = 20180228,
        returnstore = store40,
        droppedoff = 'TRUE',
        customerid = 15199,
        carid = 14904)
    order6.save()

    order7 = Orders(createdate = 20180228,
        pickupdate = 20180305,
        pickupstore = store36,
        returndate = 20180401,
        returnstore = store32,
        droppedoff = 'FALSE',
        customerid = 11459,
        carid = 15280)
    order7.save()

    order8 = Orders(createdate = 20180301,
        pickupdate = 20180303,
        pickupstore = store6,
        returndate = 20180320,
        returnstore = store6,
        droppedoff = 'TRUE',
        customerid = 11350,
        carid = 15307)
    order8.save()

    order9 = Orders(createdate = 20180404,
        pickupdate = 20180422,
        pickupstore = store21,
        returndate = 20180423,
        returnstore = store21,
        droppedoff = 'TRUE',
        customerid = 11217,
        carid = 15342)
    order9.save()

    order10 = Orders(createdate = 20180404,
        pickupdate = 20180504,
        pickupstore = store10,
        returndate = 20180513,
        returnstore = store15,
        droppedoff = 'TRUE',
        customerid = 11254,
        carid = 15307)
    order10.save()

    order11 = Orders(createdate = 20180601,
        pickupdate = 20180617,
        pickupstore = store12,
        returndate = 20180820,
        returnstore = store19,
        droppedoff = 'TRUE',
        customerid = 11158,
        carid = 14926)
    order11.save()

    order12 = Orders(createdate = 20180509,
        pickupdate = 20180522,
        pickupstore = store25,
        returndate = 2018601,
        returnstore = store25,
        droppedoff = 'TRUE',
        customerid = 11358,
        carid = 15000)
    order12.save()

    order13 = Orders(createdate = 20180625,
        pickupdate = 20180723,
        pickupstore = store33,
        returndate = 20180808,
        returnstore = store33,
        droppedoff = 'TRUE',
        customerid = 11210,
        carid = 15024)
    order13.save()

    order14 = Orders(createdate = 20180419,
        pickupdate = 20180722,
        pickupstore = store27,
        returndate = 20180723,
        returnstore = store29,
        droppedoff = 'FALSE',
        customerid = 11153,
        carid = 15307)
    order14.save()

    order15 = Orders(createdate = 20180812,
        pickupdate = 20180828,
        pickupstore = store9,
        returndate = 20180901,
        returnstore = store10,
        droppedoff = 'TRUE',
        customerid = 11114,
        carid = 15066)
    order15.save()

    order16 = Orders(createdate = 20180829,
        pickupdate = 20180902,
        pickupstore = store27,
        returndate = 20180905,
        returnstore = store31,
        droppedoff = 'TRUE',
        customerid = 11557,
        carid = 15125)
    order16.save()

    order17 = Orders(createdate = 20180914,
        pickupdate = 20180915,
        pickupstore = store28,
        returndate = 20180930,
        returnstore = store28,
        droppedoff = 'TRUE',
        customerid = 11416,
        carid = 11210)
    order17.save()

    order18 = Orders(createdate = 20180909,
        pickupdate = 20180930,
        pickupstore = store29,
        returndate = 20181031,
        returnstore = store26,
        droppedoff = 'FALSE',
        customerid = 11050,
        carid = car2)
    order18.save()

    order19 = Orders(createdate = 20180605,
        pickupdate = 20181007,
        pickupstore = store14,
        returndate = 20181112,
        returnstore = store14,
        droppedoff = 'FALSE',
        customerid = 11111,
        carid = 11350)
    order19.save()

    order20 = Orders(createdate = 20180512,
        pickupdate = 20181023,
        pickupstore = store33,
        returndate = 20181028,
        returnstore = store33,
        droppedoff = 'FALSE',
        customerid = 11515,
        carid = 15081)
    order20.save()

    order21 = Orders(createdate = 20181001,
        pickupdate = 20181003,
        pickupstore = store1,
        returndate = 20181103,
        returnstore = store12,
        droppedoff = 'FALSE',
        customerid = 11250,
        carid = 15107)
    order21.save()

    order22 = Orders(createdate = 20180808,
        pickupdate = 20181020,
        pickupstore = store27,
        returndate = 20181101,
        returnstore = store15,
        droppedoff = 'FALSE',
        customerid = 11217,
        carid = 15400)
    order22.save()

    order23 = Orders(createdate = 20180831,
        pickupdate = 20181017,
        pickupstore = store34,
        returndate = 20181105,
        returnstore = store3,
        droppedoff = 'FALSE',
        customerid = 11353,
        carid = 15024)
    order23.save()
