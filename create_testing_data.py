from ..models import *

def CreateTestData():
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

    	# Car 1
        car1 = Cars(car_makename='VOLKSWAGEN',
            car_model='GOLF',
            car_series='1K 2.0 FSI COMFORTLINE',
            car_seriesyear = 2005,
            car_pricenew = 32290,
            car_enginesize = '2.0L',
            car_fuelsystem = 'ELECTRONIC F/INJ',
            car_tankcapacity = '55L',
            car_power = '110Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '6ATip',
            car_bodytype = '5D HATCHBACK',
            car_drive = 'FWD',
            car_wheelbase = '2578mm')
        car1.save()

        # Car 2
        car2 = Cars(car_makename='VOLKSWAGEN',
            car_model='GOLF',
            car_series='1K 2.0 TDI COMFORTLINE',
            car_seriesyear = 2007,
            car_pricenew = 32490,
            car_enginesize = '2.0L',
            car_fuelsystem = 'DIESEL TURBO F/INJ',
            car_tankcapacity = '55L',
            car_power = '103Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '6M',
            car_bodytype = '5D HATCHBACK',
            car_drive = 'FWD',
            car_wheelbase = '2578mm')
        car2.save()

    	# Car 3
        car3 = Cars(car_makename='BMW',
            car_model='3',
            car_series='E36 28i',
            car_seriesyear = 1996,
            car_pricenew = 83330,
            car_enginesize = '2.8L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '65L',
            car_power = '142Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5A',
            car_bodytype = '4D SEDAN',
            car_drive = 'RWD',
            car_wheelbase = '2700mm')
        car3.save()

        # Car 4
        car4 = Cars(car_makename='BMW',
            car_model='3',
            car_series='E36 16i OPEN AIR',
            car_seriesyear = 1995,
            car_pricenew = 46200,
            car_enginesize = '1.6L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '52L',
            car_power = '75Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5M',
            car_bodytype = '3D HATCHBACK',
            car_drive = 'RWD',
            car_wheelbase = '2700mm')
        car4.save()

    	# Car 5
        car5 = Cars(car_makename='PEUGEOT',
            car_model='206',
            car_series='CC',
            car_seriesyear = 2006,
            car_pricenew = 34990,
            car_enginesize = '1.6L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '50L',
            car_power = '80Kw',
            car_seatingcapacity = 4,
            car_standardtransmission = '4ATip',
            car_bodytype = '2D CABRIOLET',
            car_drive = 'FWD',
            car_wheelbase = '2442mm')
        car5.save()

    	# Car 6
        car6 = Cars(car_makename='VOLVO',
            car_model='S40',
            car_series='MY06 T5 AWD',
            car_seriesyear = 2006,
            car_pricenew = 54950,
            car_enginesize = '2.5L',
            car_fuelsystem = 'TURBO MPFI',
            car_tankcapacity = '57L',
            car_power = '162Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5AG',
            car_bodytype = '4D SEDAN',
            car_drive = 'AWD',
            car_wheelbase = '2640mm')
        car6.save()

    	# Car 7
        car7 = Cars(car_makename='MITSUBISHI',
            car_model='380',
            car_series='DB',
            car_seriesyear = 2005,
            car_pricenew = 35990,
            car_enginesize = '3.8L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '67L',
            car_power = '175Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5ASPM',
            car_bodytype = '4D SEDAN',
            car_drive = 'FWD',
            car_wheelbase = '2750mm')
        car7.save()

    	# Car 8
        car8 = Cars(car_makename='AUDI',
            car_model='A4',
            car_series='B6 2.0 AVANT',
            car_seriesyear = 2003,
            car_pricenew = 54250,
            car_enginesize = '2.0L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '70L',
            car_power = '96Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = 'CVTM6',
            car_bodytype = '4D WAGON',
            car_drive = 'FWD',
            car_wheelbase = '2650mm')
        car8.save()

    	# Car 9
        car9 = Cars(car_makename='MERCEDES-BENZ',
            car_model='CLK230',
            car_series='KOMP ELEGANCE',
            car_seriesyear = 2000,
            car_pricenew = 111580,
            car_enginesize = '2.3L',
            car_fuelsystem = 'SUPERCHARGED MPFI',
            car_tankcapacity = '62L',
            car_power = '142Kw',
            car_seatingcapacity = 4,
            car_standardtransmission = '5A',
            car_bodytype = '2D CABRIOLET',
            car_drive = 'RWD',
            car_wheelbase = '2690mm')
        car9.save()

    	# Car 10
        car10 = Cars(car_makename='MERCEDES-BENZ',
            car_model='ML',
            car_series='W163 500 LUXURY 4x4',
            car_seriesyear = 2001,
            car_pricenew = 98500,
            car_enginesize = '5.0L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '83L',
            car_power = '215Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5ATS',
            car_bodytype = '4D WAGON',
            car_drive = '4WD',
            car_wheelbase = '2820mm')
        car10.save()

    	# Car 11
        car11 = Cars(car_makename='NISSAN',
            car_model='200',
            car_series='SX SPORTS LIMITED',
            car_seriesyear = 1994,
            car_pricenew = 38500,
            car_enginesize = '2.0L',
            car_fuelsystem = 'TURBO MPFI',
            car_tankcapacity = '65L',
            car_power = '147Kw',
            car_seatingcapacity = 4,
            car_standardtransmission = '5M',
            car_bodytype = '2D COUPE',
            car_drive = 'RWD',
            car_wheelbase = '2525mm')
        car11save()

    	# Car 12
        car12 = Cars(car_makename='AUDI',
            car_model='A6',
            car_series='4B 2.4 V6',
            car_seriesyear = 2003,
            car_pricenew = 80900,
            car_enginesize = '2.4L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '70L',
            car_power = '125Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = 'CVTM6',
            car_bodytype = '4D SEDAN',
            car_drive = 'FWD',
            car_wheelbase = '2749mm')
        car12.save()

    	# Car 13
        car13 = Cars(car_makename='CHRYSLER',
            car_model='300C',
            car_series='LE MY06 CRD',
            car_seriesyear = 2006,
            car_pricenew = 57990,
            car_enginesize = '3.0L',
            car_fuelsystem = 'DIESEL TURBO F/INJ',
            car_tankcapacity = '71L',
            car_power = '160Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5A',
            car_bodytype = '4D SEDAN',
            car_drive = 'RWD',
            car_wheelbase = '3050mm')
        car13.save()

    	# Car 14
        car14 = Cars(car_makename='LAND ROVER',
            car_model='DISCOVERY',
            car_series='SERIES II S 4x4',
            car_seriesyear = 2003,
            car_pricenew = 55450,
            car_enginesize = '4.0L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '93L',
            car_power = '136Kw',
            car_seatingcapacity = 7,
            car_standardtransmission = '4A',
            car_bodytype = '4D WAGON',
            car_drive = '4WD',
            car_wheelbase = '2540mm')
        car14.save()

    	# Car 15
        car15 = Cars(car_makename='TOYOTA',
            car_model='4 RUNNER',
            car_series='DELUXE 4x4',
            car_seriesyear = 1989,
            car_pricenew = 28200,
            car_enginesize = '2.4L',
            car_fuelsystem = 'CARB',
            car_tankcapacity = '65L',
            car_power = '75Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5M4x4',
            car_bodytype = '4D WAGON',
            car_drive = '4WD',
            car_wheelbase = '2625mm')
        car15.save()

    	# Car 16
        car16 = Cars(car_makename='NISSAN',
            car_model='200',
            car_series='SX LUXURY',
            car_seriesyear = 1998,
            car_pricenew = 49995,
            car_enginesize = '2.0L',
            car_fuelsystem = 'TURBO MPFI',
            car_tankcapacity = '65L',
            car_power = '147Kw',
            car_seatingcapacity = 4,
            car_standardtransmission = '5M',
            car_bodytype = '2D COUPE',
            car_drive = 'RWD',
            car_wheelbase = '2525mm')
        car16.save()

    	# Car 17
        car17 = Cars(car_makename='ALFA ROMEO',
            car_model='156',
            car_series='2.0 SELESPEED TWIN SPARK',
            car_seriesyear = 1999,
            car_pricenew = 49950,
            car_enginesize = '2.0L',
            car_fuelsystem = 'MULTI POINT F/INJI',
            car_tankcapacity = '63L',
            car_power = '114Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '5MSel',
            car_bodytype = '4D SEDAN',
            car_drive = 'FWD',
            car_wheelbase = '2595mm')
        car17.save()

    	# Car 18
        car18 = Cars(car_makename='MAZDA',
            car_model='929',
            car_series='LUXURY',
            car_seriesyear = 1986,
            car_pricenew = 29600,
            car_enginesize = '2.0L',
            car_fuelsystem = 'MULTI POINT F/INJ',
            car_tankcapacity = '60L',
            car_power = '70Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '4A',
            car_bodytype = '2D HARDTOP',
            car_drive = 'RWD',
            car_wheelbase = '2615mm')
        car18.save()

    	# Car 19
        car19 = Cars(car_makename='AUDI',
            car_model='S3',
            car_series='1.8',
            car_seriesyear = 2000,
            car_pricenew = 65850,
            car_enginesize = '1.8L',
            car_fuelsystem = 'TURBO MPFI',
            car_tankcapacity = '62L',
            car_power = '154Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '6M',
            car_bodytype = '3D HATCHBACK',
            car_drive = 'AWD',
            car_wheelbase = '2519mm')
        car19.save()

    	# Car 20
        car20 = Cars(car_makename='BMW',
            car_model='X5',
            car_series='E53 MY06 UPGRADE 3.0d',
            car_seriesyear = 2006,
            car_pricenew = 86800,
            car_enginesize = '3.0L',
            car_fuelsystem = 'TURBO CDI',
            car_tankcapacity = '93L',
            car_power = '150Kw',
            car_seatingcapacity = 5,
            car_standardtransmission = '6A',
            car_bodytype = '4D WAGON',
            car_drive = '4WD',
            car_wheelbase = '2820mm')
        car20.save()


        # I will need 5-10 customers. Some similar customers will have to be created,
        # such that they have similar date of births (within 5 years), a few with
        # the same occupation, and make sure gender is either M or F
        # dob needs to be of the format DD-MM-YYYY

    	# Customer 1
        customer1 = Customers(name = 'Chloe Smith',
            phone = '0423674017',
            address = '47 Tank Drive St Capalaba',
            dob = '20-04-1995',
            occupation = 'Hairdresser',
            gender = 'F',
            email = 'chloe@gmail.com',
            password = 'Chloe')
        customer1.save()
    	# Customer 2
        customer2 = Customers(name = 'Daniel Jones',
            phone = '0409638910',
            address = '16 Sunnyvale Way Carindale',
            dob = '13-11-1987',
            occupation = 'Plumber',
            gender = 'M',
            email = 'daniel@gmail.com',
            password = 'Daniel')
        customer2.save()

     	# Customer 3
        customer3 = Customers(name = 'Sarah Lee',
            phone = '0456781109',
            address = '2 Parkside Road Forestlake',
            dob = '06-01-1990',
            occupation = 'Hairdresser',
            gender = 'F',
            email = 'sarah@gmail.com',
            password = 'Sarah')
        customer3.save()

     	# Customer 4
        customer4 = Customers(name = 'Raymond',
            phone = '04117892034',
            address = '123 Green Wood St Drewvale',
            dob = '20-04-1995',
            occupation = 'Accountant',
            gender = 'M',
            email = 'raymond@gmail.com',
            password = 'Raymond')
        customer4.save()

     	# Customer 5
        customer5 = Customers(name = 'Ivan Wong',
            phone = '0478882100',
            address = '8 Coldwater Place Carindale',
            dob = '30-12-1986',
            occupation = 'Doctor',
            gender = 'M',
            email = 'ivan@gmail.com',
            password = 'Ivan')
        customer5.save()

     	# Customer 6
        customer6 = Customers(name = 'Alyssa Hi',
            phone = '0412345098',
            address = '234 Conner Place Northlakes',
            dob = '19-07-1990',
            occupation = 'Teacher',
            gender = 'F',
            email = 'alyssa@gmail.com',
            password = 'Alyssa')
        customer6.save()

     	# Customer 7
        customer7 = Customers(name = 'Caleb Lee',
            phone = '0432155566',
            address = '190 Fine Drive Browns Plains',
            dob = '05-11-1992',
            occupation = 'Painter',
            gender = 'M',
            email = 'caleb@gmail.com',
            password = 'Caleb')
        customer7.save()

     	# Customer 8
        customer8 = Customers(name = 'Zoe Gee',
            phone = '0499907654',
            address = '33 Duke Way Loganhome',
            dob = '21-10-1968',
            occupation = 'Teacher',
            gender = 'F',
            email = 'zoe@gmail.com',
            password = 'Zoe')
        customer8.save()

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
        carid = car16)
    order1.save()

    order2 = Orders(createdate = 20180703,
        pickupdate = 20180704,
        pickupstore = store2,
        returndate = 20180820,
        returnstore = store1,
        droppedoff = 'FALSE',
        customerid = customer1,
        carid = car15)
    order2.save()

    order3 = Orders(createdate = 20181018,
        pickupdate = 20181020,
        pickupstore = store17,
        returndate = 20181103,
        returnstore = store17,
        droppedoff = 'FALSE',
        customerid = customer1,
        carid = car14)
    order3.save()

    order4 = Orders(createdate = 20180101,
        pickupdate = 20180101,
        pickupstore = store3,
        returndate = 20180901,
        returnstore = store12,
        droppedoff = 'TRUE',
        customerid = customer1,
        carid = car13)
    order4.save()

    order5 = Orders(createdate = 20180201,
        pickupdate = 20180214,
        pickupstore = store1,
        returndate = 20180217,
        returnstore = store1,
        droppedoff = 'TRUE',
        customerid = customer1,
        carid = car12)
    order5.save()

    order6 = Orders(createdate = 20180217,
        pickupdate = 20180221,
        pickupstore = store1,
        returndate = 20180228,
        returnstore = store2,
        droppedoff = 'TRUE',
        customerid = customer1,
        carid = car11)
    order6.save()

    order7 = Orders(createdate = 20180228,
        pickupdate = 20180305,
        pickupstore = store2,
        returndate = 20180401,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer1,
        carid = car11)
    order7.save()

    order8 = Orders(createdate = 20180301,
        pickupdate = 20180303,
        pickupstore = store1,
        returndate = 20180320,
        returnstore = store2,
        droppedoff = 'TRUE',
        customerid = customer1,
        carid = car10)
    order8.save()

    order9 = Orders(createdate = 20180404,
        pickupdate = 20180422,
        pickupstore = store2,
        returndate = 20180423,
        returnstore = store1,
        droppedoff = 'TRUE',
        customerid = customer1,
        carid = car9)
    order9.save()

    order10 = Orders(createdate = 20180404,
        pickupdate = 20180504,
        pickupstore = store1,
        returndate = 20180513,
        returnstore = store1,
        droppedoff = 'TRUE',
        customerid = customer2,
        carid = car8)
    order10.save()

    order11 = Orders(createdate = 20180601,
        pickupdate = 20180617,
        pickupstore = store2,
        returndate = 20180820,
        returnstore = store2,
        droppedoff = 'TRUE',
        customerid = customer2,
        carid = car7)
    order11.save()

    order12 = Orders(createdate = 20180509,
        pickupdate = 20180522,
        pickupstore = store2,
        returndate = 2018601,
        returnstore = store2,
        droppedoff = 'TRUE',
        customerid = customer2,
        carid = car6)
    order12.save()

    order13 = Orders(createdate = 20180625,
        pickupdate = 20180723,
        pickupstore = store2,
        returndate = 20180808,
        returnstore = store1,
        droppedoff = 'TRUE',
        customerid = customer3,
        carid = car6)
    order13.save()

    order14 = Orders(createdate = 20180419,
        pickupdate = 20180722,
        pickupstore = store1,
        returndate = 20180723,
        returnstore = store1,
        droppedoff = 'FALSE',
        customerid = customer3,
        carid = car6)
    order14.save()

    order15 = Orders(createdate = 20180812,
        pickupdate = 20180828,
        pickupstore = store1,
        returndate = 20180901,
        returnstore = store1,
        droppedoff = 'TRUE',
        customerid = customer3,
        carid = car5)
    order15.save()

    order16 = Orders(createdate = 20180829,
        pickupdate = 20180902,
        pickupstore = store2,
        returndate = 20180905,
        returnstore = store1,
        droppedoff = 'TRUE',
        customerid = customer4,
        carid = car4)
    order16.save()

    order17 = Orders(createdate = 20180914,
        pickupdate = 20180915,
        pickupstore = store2,
        returndate = 20180930,
        returnstore = store2,
        droppedoff = 'TRUE',
        customerid = customer4,
        carid = car3)
    order17.save()

    order18 = Orders(createdate = 20180909,
        pickupdate = 20180930,
        pickupstore = store1,
        returndate = 20181031,
        returnstore = store1,
        droppedoff = 'FALSE',
        customerid = customer5,
        carid = car2)
    order18.save()

    order19 = Orders(createdate = 20180605,
        pickupdate = 20181007,
        pickupstore = store1,
        returndate = 20181112,
        returnstore = store1,
        droppedoff = 'FALSE',
        customerid = customer6,
        carid = car2)
    order19.save()

    order20 = Orders(createdate = 20180512,
        pickupdate = 20181023,
        pickupstore = store2,
        returndate = 20181028,
        returnstore = store1,
        droppedoff = 'FALSE',
        customerid = customer6,
        carid = car2)
    order20.save()

    order21 = Orders(createdate = 20181001,
        pickupdate = 20181003,
        pickupstore = store1,
        returndate = 20181103,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer7,
        carid = car2)
    order21.save()

    order22 = Orders(createdate = 20180808,
        pickupdate = 20181020,
        pickupstore = store2,
        returndate = 20181101,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer7,
        carid = car1)
    order22.save()

    order23 = Orders(createdate = 20180831,
        pickupdate = 20181017,
        pickupstore = store2,
        returndate = 20181105,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer8,
        carid = car1)
    order23.save()

    order24 = Orders(createdate = 20181001,
        pickupdate = 20181003,
        pickupstore = store1,
        returndate = 20181103,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer7,
        carid = car20)
    order24.save()

    order25 = Orders(createdate = 20180808,
        pickupdate = 20181020,
        pickupstore = store2,
        returndate = 20181101,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer7,
        carid = car19)
    order25.save()

    order26 = Orders(createdate = 20180831,
        pickupdate = 20181017,
        pickupstore = store2,
        returndate = 20181105,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer8,
        carid = car18)
    order26.save()

    order27 = Orders(createdate = 20180831,
        pickupdate = 20181017,
        pickupstore = store2,
        returndate = 20181105,
        returnstore = store2,
        droppedoff = 'FALSE',
        customerid = customer8,
        carid = car17)
    order27.save()
