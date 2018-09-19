from ..models import *
from .inputVerification import *
from .timeobjects import *
import math
from itertools import chain

def vehicleToBeReturned(request):
    # Constants delaration
    STARTDATE = 'start_date'
    RETURNSTORE = 'returnStore'
    ORDERING = 'ordering'
    DATE = 'date'
    NUM = 'num'
    YMD = 'YMD'
    RETURNDATE = 'returndate'
    DAILY = 'daily'
    MONTHLY = 'monthly'

    start_date = []
    inputVeriObj = inputVerification(request)
    if inputVeriObj.checkFormGET(STARTDATE, DATE):
        inputtedDate = givenTime(request.GET[STARTDATE], YMD)
    else:
        inputtedDate = currentTime()
    start_date.append(inputtedDate.getDate())

    # test values NEEDS TO BE DELETED
    start_date[0] = 20050711
    
    ordersToBeReturned = Orders.objects.filter(returndate__gte=start_date[0])
    if inputVeriObj.checkFormGET(RETURNSTORE, NUM):
        ordersToBeReturned = ordersToBeReturned.filter(returnstore=request.GET[RETURNSTORE])
    ordersToBeReturned = ordersToBeReturned.order_by(RETURNDATE)

    if inputVeriObj.checkFormGET(ORDERING, ''):
        if request.GET[ORDERING] == DAILY:
            sortLength = 1
            start_date[0] = start_date[0] + sortLength
        elif request.GET[ORDERING] == MONTHLY:
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
    carInfo = []
    customerInfo = []
    storeInfo = []
    for order in ordersToBeReturned:
        difference = order.returndate - start_date[counter]
        carInfo = list(chain(carInfo, Cars.objects.filter(id=order.carid_id)))
        customerInfo = list(chain(customerInfo, Customers.objects.filter(id=order.customerid_id)))
        storeInfo = list(chain(storeInfo, Stores.objects.filter(id=order.returnstore_id)))
        if difference <= 0:
            start_date.append(start_date[counter])
        else:
            start_date.append(start_date[counter] + math.ceil(difference/sortLength)*sortLength)
        counter = counter + 1
    zippedResults = zip(ordersToBeReturned, start_date, carInfo, customerInfo, storeInfo)
    return zippedResults
