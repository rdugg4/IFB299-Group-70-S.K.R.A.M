from ..models import *
from .inputVerification import *
from .timeobjects import *
from django.db.models import Max

def searchData(request):
    resultantOrders = Orders.objects.all()
    ordersToExclude = resultantOrders.none()
    if request.method == 'GET':
        # Constants declaration
        PICKUPDATE = 'pickupDate'
        DROPOFFDATE = 'dropoffDate'
        PICKUPLOCATION = 'pickupLocation'
        SEATS = 'seats'
        DRIVETYPE = 'driveType'
        MAKEOFCAR = 'makeOfCar'
        CARMODEL = 'carModel'
        BODYTYPE = 'bodyType'

        DATE = 'date'
        NUM = 'num'
        YMD = 'YMD'

        inputVeriObj = inputVerification(request)
        resultantCars = Cars.objects.all()

        if inputVeriObj.checkFormGET(PICKUPDATE, DATE):
            inputtedDate = givenTime(request.GET[PICKUPDATE], YMD)
        else:
            inputtedDate = currentTime()
        pickupDate_int = inputtedDate.getDate()

        if inputVeriObj.checkFormGET(DROPOFFDATE, DATE):
            inputtedDropOffDate = givenTime(request.GET[DROPOFFDATE], YMD)
        else:
            inputtedDropOffDate = timeObject(30000101)
        dropoffDate_int = inputtedDropOffDate.getDate()

        carsFinalLocation = Orders.objects.none()
        for car in Cars.objects.all():
            maximum = resultantOrders.filter(carid_id=car.id).aggregate(max_date = Max('returndate'))['max_date']
            carsFinalLocation = carsFinalLocation | resultantOrders.filter(carid_id=car.id, returndate=maximum)
        resultantOrders = carsFinalLocation

        if inputVeriObj.checkFormGET(PICKUPLOCATION, NUM):
            ordersFinishedAtPickupLocation = resultantOrders.filter(returnstore=request.GET['pickupLocation'])
            ordersToExclude = resultantOrders.exclude(id__in=ordersFinishedAtPickupLocation)

        ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=pickupDate_int, pickupdate__lte=pickupDate_int)
        ordersToExclude = ordersToExclude | resultantOrders.filter(returndate__gte=dropoffDate_int, pickupdate__lte=dropoffDate_int)

        ordersToBeReturned = resultantOrders.exclude(id__in=ordersToExclude)
        resultantCars = Cars.objects.none()
        for order in ordersToBeReturned:
            resultantCars = resultantCars | Cars.objects.filter(id=order.carid_id)

        if inputVeriObj.checkFormGET(SEATS, NUM):
            if int(request.GET['seats']) == 8:
                resultantCars = resultantCars.filter(car_seatingcapacity__gte=request.GET['seats'])
            elif int(request.GET['seats']) == 3:
                resultantCars = resultantCars.filter(car_seatingcapacity__lte=request.GET['seats'])
            else:
                resultantCars = resultantCars.filter(car_seatingcapacity=request.GET['seats'])

        if inputVeriObj.checkFormGET(DRIVETYPE, ''):
            resultantCars = resultantCars.filter(car_drive__icontains=request.GET['driveType'])

        if inputVeriObj.checkFormGET(MAKEOFCAR, ''):
            resultantCars = resultantCars.filter(car_makename__icontains=request.GET['makeOfCar'])

        if inputVeriObj.checkFormGET(CARMODEL, ''):
            resultantCars = resultantCars.filter(car_model__icontains=request.GET['carModel'])

        if inputVeriObj.checkFormGET(BODYTYPE, ''):
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
    return resultantCars
