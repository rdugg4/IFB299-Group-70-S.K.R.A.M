from django.shortcuts import render
from .models import Cars
from .models import Customers
from .models import Stores
from .models import Orders
import math
from django.db.models import Max
from django.http import HttpResponse
from .functions.timeobjects import *


def index(request):
    storelist = Stores.objects.all()
    context = {'StoreList': storelist}
    return render(request, 'testApp/index.html', context)

def detail(request, car_id):
    carInfo = Cars.objects.filter(id=car_id)
    context = {'CarInfo': carInfo}
    return render(request, 'testApp/carDetails.html', context)

def accounts(request):
    if request.method == "POST":
        if (request.POST.get('Name') and request.POST.get('Phone') and request.POST.get('Address') and request.POST.get('DOB') and request.POST.get('Occupation') and request.POST.get('Gender') and request.POST.get('Email') and request.POST.get('Password')):
            post = Customers()
            post.name = request.POST.get('Name')
            post.phone = request.POST.get('Phone')
            post.address = request.POST.get('Address')
            post.dob = request.POST.get('DOB')
            post.occupation = request.POST.get('Occupation')
            post.gender = request.POST.get('Gender')
            post.email = request.POST.get('Email')
            post.password = request.POST.get('Password')
            post.save()
            return render(request, 'testApp/signup.html')
        else:
            return render(request,'testApp/signup.html')
    else:
        return render(request,'testApp/signup.html')

def staffPortal(request):
    return render(request, 'testApp/staffPortal.html')

def returnPage(request):

    inputtedDate = timeObject(0)
    start_date = []
    if (('start_date' in request.GET) and (request.GET['start_date']) and (isint(request.GET['start_date'][0:4]))
        and (isint(request.GET['start_date'][5:7])) and (isint(request.GET['start_date'][8:10]))):
        inputtedDate = givenTime(request.GET['start_date'], 'YMD')
    else:
        inputtedDate = currentTime()
    start_date.append(inputtedDate.getDate())

    ordersToBeReturned = Orders.objects.filter(returndate__gte=start_date[0])
    if ('returnStore' in request.GET) and (request.GET['returnStore']) and (isint(request.GET['returnStore'])):
        ordersToBeReturned = ordersToBeReturned.filter(returnstore=request.GET['returnStore'])
    ordersToBeReturned = ordersToBeReturned.order_by('returndate')

    if ('ordering' in request.GET) and (request.GET['ordering']):
        if request.GET['ordering'] == 'daily':
            sortLength = 1
            start_date[0] = start_date[0] + sortLength
        elif request.GET['ordering'] == 'monthly':
            sortLength = 100
            start_date[0] = start_date[0] + (sortLength - sortLength/2)
        else:
            sortLength = 7
            weekday = inputtedDate.weekday()
            start_date[0] = start_date[0] + (sortLength - weekday)
    else:
        sortLength = 7
        weekday = inputtedDate.weekday()
        start_date[0] = start_date[0] + (sortLength - weekday)

    counter = 0
    for order in ordersToBeReturned:
        difference = order.returndate - start_date[counter]
        if difference <= 0:
            start_date.append(start_date[counter])
        else:
            start_date.append(start_date[counter] + math.ceil(difference/sortLength)*sortLength)
        counter = counter + 1
    zippedResults = zip(ordersToBeReturned, start_date)
    storelist = Stores.objects.all()
    context = {'zippedResults': zippedResults, 'StoreList': storelist}
    return render(request, 'testApp/returnPage.html', context)

def search(request):
    resultantOrders = Orders.objects.all()
    ordersToExclude = resultantOrders.none()
    if request.method == 'GET':
        resultantCars = Cars.objects.all()
        pickupDateSet = (('pickupDate' in request.GET) and (request.GET['pickupDate']) and (isint(request.GET['pickupDate'][0:4]))
            and (isint(request.GET['pickupDate'][5:7])) and (isint(request.GET['pickupDate'][8:10])))
        dropoffDateSet = (('dropoffDate' in request.GET) and (request.GET['dropoffDate']) and (isint(request.GET['dropoffDate'][0:4]))
            and (isint(request.GET['dropoffDate'][5:7])) and (isint(request.GET['dropoffDate'][8:10])))
        pickupLocationSet = (('pickupLocation' in request.GET) and (request.GET['pickupLocation'])
            and (isint(request.GET['pickupLocation'])))

        inputtedDate = timeObject(0)
        if pickupDateSet:
            inputtedDate = givenTime(request.GET['pickupDate'], 'YMD')
        else:
            inputtedDate = currentTime()
        pickupDate_int = inputtedDate.getDate()

        inputtedDropOffDate = timeObject(0)
        if dropoffDateSet:
            inputtedDropOffDate = givenTime(request.GET['dropoffDate'], 'YMD')
        else:
            inputtedDropOffDate = timeObject(30000101)
        dropoffDate_int = inputtedDropOffDate.getDate()

        carsFinalLocation = Orders.objects.none()
        for car in Cars.objects.all():
            maximum = resultantOrders.filter(carid_id=car.id).aggregate(max_date = Max('returndate'))['max_date']
            carsFinalLocation = carsFinalLocation | resultantOrders.filter(carid_id=car.id, returndate=maximum)
        resultantOrders = carsFinalLocation

        if pickupLocationSet:
            ordersFinishedAtPickupLocation = resultantOrders.filter(returnstore=request.GET['pickupLocation'])
            ordersToExclude = resultantOrders.exclude(id__in=ordersFinishedAtPickupLocation)

        ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=pickupDate_int, pickupdate__lte=pickupDate_int)
        ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=dropoffDate_int, pickupdate__lte=dropoffDate_int)

        ordersToBeReturned = resultantOrders.exclude(id__in=ordersToExclude)
        resultantCars = Cars.objects.none()
        for order in ordersToBeReturned:
            resultantCars = resultantCars | Cars.objects.filter(id=order.carid_id)

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

    elif request.method == 'POST':
        customer = Customers.objects.filter(id=request.POST['userid'])
        for aCustomer in customer:
            similar_customers = Customers.objects.filter(gender=aCustomer.gender, occupation=aCustomer.occupation)
            aCustomerdob = givenTime(aCustomer.dob, 'DMY').getDate()

            for aCustomer2 in similar_customers:
                aCustomer2dob = givenTime(aCustomer2.dob, 'DMY').getDate()
                if (aCustomerdob <= (aCustomer2dob - 50000) or aCustomerdob >= (aCustomer2dob + 50000)):
                    similar_customers = similar_customers.exclude(id=aCustomer2.id)

        ordersBySimilarCustomers = Orders.objects.none()
        for aCustomer in similar_customers:
            ordersBySimilarCustomers = ordersBySimilarCustomers | Orders.objects.filter(customerid=aCustomer.id)
        pickupDate_int = currentTime().getDate()
        dropoffDate_int = timeObject(30000101).getDate()
        ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=pickupDate_int, pickupdate__lte=pickupDate_int)
        ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=dropoffDate_int, pickupdate__lte=dropoffDate_int)
        resultantCars = Cars.objects.none()
        for order in ordersBySimilarCustomers:
            resultantCars = resultantCars | Cars.objects.filter(id=order.carid_id)
        for order in ordersToExclude:
            resultantCars = resultantCars.exclude(id=order.carid_id)

    storelist = Stores.objects.all()
    context = {'resultantCars': resultantCars, 'StoreList': storelist}
    return render(request, 'testApp/searchResults.html', context)

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
