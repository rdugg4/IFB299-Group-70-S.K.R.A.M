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

def accounts(request):
    if request.method == "POST":
        if request.POST.get('Name') and request.POST.get('Phone') and request.POST.get('Address') and request.POST.get('DOB') and request.POST.get('Occupation') and request.POST.get('Gender') and request.POST.get('Email') and request.POST.get('Password'):
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

def staffPortal(request):
    return render(request, 'testApp/staffPortal.html')

def returnPage(request):
    return render(request, 'testApp/returnPage.html')

def search(request):
    resultantOrders = Orders.objects.all()
    ordersToExclude = resultantOrders.none()
    now = datetime.datetime.now()
    if request.method == 'GET':
        resultantCars = Cars.objects.all()
        pickupDateSet = (('pickupDate' in request.GET) and (request.GET['pickupDate']) and (isint(request.GET['pickupDate'][0:4]))
            and (isint(request.GET['pickupDate'][5:7])) and (isint(request.GET['pickupDate'][8:10])))
        dropoffDateSet = (('dropoffDate' in request.GET) and (request.GET['dropoffDate']) and (isint(request.GET['dropoffDate'][0:4]))
            and (isint(request.GET['dropoffDate'][5:7])) and (isint(request.GET['dropoffDate'][8:10])))
        pickupLocationSet = (('pickupLocation' in request.GET) and (request.GET['pickupLocation'])
            and (isint(request.GET['pickupLocation'])))
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
            dropoffDate_int = 30000101

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

        # context = {'testing': resultantCars}
        # return render(request, 'testApp/test.html', context)

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
            aCustomerdob = int(aCustomer.dob[6:10] + aCustomer.dob[3:5] + aCustomer.dob[0:2])

            for aCustomer2 in similar_customers:
                aCustomer2dob = int(aCustomer2.dob[6:10] + aCustomer2.dob[3:5] + aCustomer2.dob[0:2])
                if (aCustomerdob <= (aCustomer2dob - 50000) or aCustomerdob >= (aCustomer2dob + 50000)):
                    similar_customers = similar_customers.exclude(id=aCustomer2.id)

        ordersBySimilarCustomers = Orders.objects.none()
        for aCustomer in similar_customers:
            ordersBySimilarCustomers = ordersBySimilarCustomers | Orders.objects.filter(customerid=aCustomer.id)
        pickupDate_int = int(str(now.year)+str(now.month)+str(now.day))
        dropoffDate_int = 30000101
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
