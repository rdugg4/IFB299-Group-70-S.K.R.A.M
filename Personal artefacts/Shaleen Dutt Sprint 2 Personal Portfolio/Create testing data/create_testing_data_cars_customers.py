from ..models import *

def CreateTestData():

	
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

	

