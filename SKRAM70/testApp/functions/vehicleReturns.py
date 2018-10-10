from ..models import *
from .inputVerification import *
from .timeobjects import *
import math
from itertools import chain
from django.contrib import messages

class VehicleReturns(object):
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

        inputVeriObj = inputVerification(request)
        if inputVeriObj.checkFormGET(STARTDATE, DATE):
            inputtedDate = givenTime(request.GET[STARTDATE], YMD)
        else:
            inputtedDate = currentTime()
        start_date = inputtedDate.getDate()

        ordersToBeReturned = Orders.objects.filter(returndate__gte=start_date)
        if inputVeriObj.checkFormGET(RETURNSTORE, NUM):
            ordersToBeReturned = ordersToBeReturned.filter(returnstore=request.GET[RETURNSTORE])
        ordersToBeReturned = ordersToBeReturned.order_by(RETURNDATE)

        lengthOfGrouping = 'Week'
        if inputVeriObj.checkFormGET(ORDERING, ''):
            if request.GET[ORDERING] == DAILY:
                sortLength = 1
                start_date = start_date + sortLength
                lengthOfGrouping = 'Day'
            elif request.GET[ORDERING] == MONTHLY:
                sortLength = 100
                start_date = start_date + (sortLength - sortLength/2)
                lengthOfGrouping = 'Month'
            else:
                sortLength = 7
                weekday = inputtedDate.weekday()
                start_date = start_date + (sortLength - weekday)
        else:
            sortLength = 7
            weekday = inputtedDate.weekday()
            start_date = start_date + (sortLength - weekday)

        carInfo = []
        customerInfo = []
        storeInfo = []
        ordersGrouped = []
        orderGroup = []

        for order in ordersToBeReturned:
            difference = order.returndate - start_date
            carInfo = list(chain(carInfo, Cars.objects.filter(id=order.carid_id)))
            customerInfo = list(chain(customerInfo, Customers.objects.filter(id=order.customerid_id)))
            storeInfo = list(chain(storeInfo, Stores.objects.filter(id=order.returnstore_id)))

            if difference > 0:
                start_date = start_date + math.ceil(difference/sortLength)*sortLength
                if len(orderGroup) != 0:
                    ordersGrouped.append(orderGroup)
                    orderGroup = []

            orderGroup.append(order)

        counter = []
        setNames = []
        i = 0
        while i < 10 and len(ordersGrouped) > i:
            counter.append(len(ordersGrouped[i]))
            setNames.append('Week ' + str(i + 1))
            i = i + 1

        graphType = "None"
        if inputVeriObj.checkFormGET('Graph', 'string'):
            graphType = request.GET['Graph']
            if graphType != 'Column' and graphType != 'Pie' and graphType != 'None':
                graphType = "None"
                messages.add_message(request, messages.INFO, 'Your inputted Graph Type was not one of the options and defaulted to No Graph')


        zippedResults = zip(ordersGrouped, carInfo, customerInfo, storeInfo)
        counterAndNames = zip(counter, setNames)
        return (zippedResults, counterAndNames, graphType, lengthOfGrouping)
