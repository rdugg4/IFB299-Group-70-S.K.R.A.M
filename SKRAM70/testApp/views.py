from django.shortcuts import render
from .models import Cars
from .models import Customers
from .models import Stores
from .models import Orders
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
    resultantCars = Cars.objects.none()
    pickupDateSet = (('pickupDate' in request.GET) and (request.GET['pickupDate']) and (isint(request.GET['pickupDate'][0:4]))
        and (isint(request.GET['pickupDate'][5:7])) and (isint(request.GET['pickupDate'][8:10])))
    dropoffDataSet = (('dropoffDate' in request.GET) and (request.GET['dropoffDate']) and (isint(request.GET['dropoffDate'][0:4]))
        and (isint(request.GET['dropoffDate'][5:7])) and (isint(request.GET['dropoffDate'][8:10])))
    if ('pickupLocation' in request.GET) and (request.GET['pickupLocation']) and (isint(request.GET['pickupLocation'])):
        ordersWithCarsInLocation = Orders.objects.filter(returnstore=request.GET['pickupLocation'])
        for order in ordersWithCarsInLocation:
            # carsHaveBeenReturned = ((int(request.GET['pickupDate'][0:4]) > int(str(order.returndate)[0:4])) or
            #     ((int(request.GET['pickupDate'][0:4]) == int(str(order.returndate)[0:4]))
            #     and (int(request.GET['pickupDate'][5:7]) > int(str(order.returndate)[4:6]))) or
            #     ((int(request.GET['pickupDate'][0:4]) == int(str(order.returndate)[0:4]))
            #     and (int(request.GET['pickupDate'][5:7]) == int(str(order.returndate)[4:6]))
            #     and (int(request.GET['pickupDate'][8:10]) >= int(str(order.returndate)[6:8]))))
            # carNotOrdered = ((int(request.GET['dropoffDate'][0:4]) > int(str(order.pickupdate)[0:4])) or
            #     ((int(request.GET['dropoffDate'][0:4]) == int(str(order.pickupdate)[0:4]))
            #     and (int(request.GET['dropoffDate'][5:7]) > int(str(order.pickupdate)[4:6]))) or
            #     ((int(request.GET['dropoffDate'][0:4]) == int(str(order.pickupdate)[0:4]))
            #     and (int(request.GET['dropoffDate'][5:7]) == int(str(order.pickupdate)[4:6]))
            #     and (int(request.GET['dropoffDate'][8:10]) >= int(str(order.pickupdate)[6:8]))))
            # if (carsHaveBeenReturned):
            temp = Cars.objects.filter(id=order.carid_id)
            resultantCars = resultantCars | temp
    else:
        resultantCars = Cars.objects.all()


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
