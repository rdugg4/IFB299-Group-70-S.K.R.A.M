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
    car1 = Cars(car_makename='make',
        car_model='model',
        car_series='Series',
        car_seriesyear = 2006,
        car_pricenew = 5000,
        car_enginesize = 'eiginesize',
        car_fuelsystem = 'fuelsystem',
        car_tankcapacity = 'tankcapacity',
        car_power = 'power',
        car_seatingcapacity = 6,
        car_standardtransmission = 'Standardtransmission',
        car_bodytype = 'hatchback',
        car_drive = '4WD',
        car_wheelbase = '4000mm')
    car1.save()

    # Car 2 will likely need to be changed
    car2 = Cars(car_makename='make',
        car_model='model',
        car_series='Series',
        car_seriesyear = 2006,
        car_pricenew = 5000,
        car_enginesize = 'eiginesize',
        car_fuelsystem = 'fuelsystem',
        car_tankcapacity = 'tankcapacity',
        car_power = 'power',
        car_seatingcapacity = 6,
        car_standardtransmission = 'Standardtransmission',
        car_bodytype = 'hatchback',
        car_drive = '4WD',
        car_wheelbase = '4000mm')
    car2.save()

    # All needed stores are already created
    store1 = Stores(name = "testName",
        address = "testAdress",
        phone = "045555555",
        city = "testCity",
        state = "testState")
    store1.save()

    store2 = Stores(name = "testName2",
        address = "testAdress2",
        phone = "045555556",
        city = "testCity2",
        state = "testState2")
    store2.save()

    # I will need 5-10 customers. Some similar customers will have to be created,
    # such that they have similar date of births (within 5 years), a few with
    # the same occupation, and make sure gender is either M or F
    # dob needs to be of the format DD-MM-YYYY
    customer1 = Customers(name = "Fake Name",
        phone = '045555555',
        address = 'This is a fake address',
        dob = '20-04-1998',
        occupation = 'Plumber',
        gender = 'M',
        email = 'test@email.com',
        password = 'testpassword')
    customer1.save()

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
