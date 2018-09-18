from ..models import *
from .inputVerification import *
from .timeobjects import *
import math

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
    for order in ordersToBeReturned:
        difference = order.returndate - start_date[counter]
        if difference <= 0:
            start_date.append(start_date[counter])
        else:
            start_date.append(start_date[counter] + math.ceil(difference/sortLength)*sortLength)
        counter = counter + 1
    zippedResults = zip(ordersToBeReturned, start_date)
    return zippedResults
