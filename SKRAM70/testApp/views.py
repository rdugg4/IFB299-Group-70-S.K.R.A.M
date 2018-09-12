from django.shortcuts import render
from .models import Cars
from .models import Customers
from .models import Stores
from .models import Orders
import datetime
from django.http import HttpResponse

def index(request):
    storelist = Stores.objects.all()
    context = {'StoreList': storelist}
    return render(request, 'testApp/index.html', context)

def detail(request, car_id):
    carInfo = Cars.objects.filter(id=car_id)
    context = {'CarInfo': carInfo}
    return render(request, 'testApp/carDetails.html', context)

def accounts(request, customer_id):
    customer = Customers.objects.filter(id=customer_id)
    context = {'Customer': customer}
    return render(request, 'testApp/signup.html', context)

def search(request):
    resultantCars = Cars.objects.all()
    resultantOrders = Orders.objects.all()
    ordersToExclude = resultantOrders.none()
    pickupDateSet = (('pickupDate' in request.GET) and (request.GET['pickupDate']) and (isint(request.GET['pickupDate'][0:4]))
        and (isint(request.GET['pickupDate'][5:7])) and (isint(request.GET['pickupDate'][8:10])))
    dropoffDateSet = (('dropoffDate' in request.GET) and (request.GET['dropoffDate']) and (isint(request.GET['dropoffDate'][0:4]))
        and (isint(request.GET['dropoffDate'][5:7])) and (isint(request.GET['dropoffDate'][8:10])))
    pickupLocationSet = (('pickupLocation' in request.GET) and (request.GET['pickupLocation'])
        and (isint(request.GET['pickupLocation'])))
    now = datetime.datetime.now()
    pickupDate_int = 0
    if pickupDateSet:
        pickupDate_string = request.GET['pickupDate'][0:4] + request.GET['pickupDate'][5:7] + request.GET['pickupDate'][8:10]
        pickupDate_int = int(pickupDate_string)
    else:
        pickupDate_int = int(str(now.year)+str(now.month)+str(now.day))

    if dropoffDateSet:
        dropoffDate_string = request.GET['dropoffDate'][0:4] + request.GET['dropoffDate'][5:7] + request.GET['dropoffDate'][8:10]
        dropoffDate_int = int(dropoffDate_string)
    else:
        dropoffDate_int == 30000101

    if pickupLocationSet:
        ordersFinishedAtPickupLocation = resultantOrders.filter(returnstore=request.GET['pickupLocation'])
        # for order in ordersFinishedAtPickupLocation:
        #     carID = order.carid_id
        #     ordersUsingAParticularCar = resultantOrders.filter(carid_id=carID)
        #     mostRecentID = 0
        #     mostRecentDate = 0
        #     for order2 in ordersUsingAParticularCar:
        #         if (order2.returndate > mostRecentDate and order2.returndate < pickupDate_int):
        #             mostRecentID = order2.id
        #             mostRecentDate = order2.returndate
        ordersToExclude = resultantOrders.exclude(id__in=ordersFinishedAtPickupLocation)



    ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=pickupDate_int, pickupdate__lte=pickupDate_int)
    ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=dropoffDate_int, pickupdate__lte=dropoffDate_int)

    for order in ordersToExclude:
        resultantCars = resultantCars.exclude(id=order.carid_id)

    context = {'testing': resultantCars}
    return render(request, 'testApp/test.html', context)

    if ('seats' in request.GET) and (request.GET['seats']) and (isint(request.GET['seats'])):
        if int(request.GET['seats']) == 8:
            resultantCars = resultantCars.filter(car_seatingcapacity__gte=request.GET['seats'])
        elif int(request.GET['seats']) == 3:
            resultantCars = resultantCars.filter(car_seatingcapacity__lte=request.GET['seats'])
        else:
            resultantCars = resultantCars.filter(car_seatingcapacity=request.GET['seats'])

    if ('driveType' in request.GET) and (request.GET['driveType']):
        resultantCars = resultantCars.filter(car_drive__icontains=request.GET['driveType'])

    if ('makeOfCar' in request.GET) and (request.GET['makeOfCar']):
        resultantCars = resultantCars.filter(car_makename__icontains=request.GET['makeOfCar'])

    if ('carModel' in request.GET) and (request.GET['carModel']):
        resultantCars = resultantCars.filter(car_model__icontains=request.GET['carModel'])

    if ('bodyType' in request.GET) and (request.GET['bodyType']):
        resultantCars = resultantCars.filter(car_bodytype__icontains=request.GET['bodyType'])

    context = {'resultantCars': resultantCars}
    return render(request, 'testApp/searchResults.html', context)

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
