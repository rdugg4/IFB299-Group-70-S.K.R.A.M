from ..models import *
from .inputVerification import *
from .timeobjects import *
import math
from django.contrib import messages
from .userVerification import *

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

        startDateFormattedForReturn = ''
        inputVeriObj = inputVerification(request)
        if inputVeriObj.checkFormGET(STARTDATE, DATE):
            inputtedDate = givenTime(request.GET[STARTDATE], YMD)
            startDateFormattedForReturn = request.GET[STARTDATE]
        else:
            inputtedDate = currentTime()
        start_date = inputtedDate.getDate()

        ordersToBeReturned = Orders.objects.filter(returndate__gte=start_date)
        storeIDformatted = ''
        if UserVerification.BoardMemberLoggedIn(request):
            if inputVeriObj.checkFormGET(RETURNSTORE, NUM):
                ordersToBeReturned = ordersToBeReturned.filter(returnstore=request.GET[RETURNSTORE])
                storeIDformatted = request.GET[RETURNSTORE]
            ordersToBeReturned = ordersToBeReturned.order_by(RETURNDATE)
        elif UserVerification.StaffLoggedIn(request):
            staffProfile = StaffMembers.objects.get(user = request.user)
            ordersToBeReturned = ordersToBeReturned.filter(returnstore=staffProfile.storeid)
        else:
            ordersToBeReturned.none()

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

        counter = []
        setNames = []
        i = 1

        for order in ordersToBeReturned:
            difference = order.returndate - start_date
            if difference > 0:
                start_date = start_date + math.ceil(difference/sortLength)*sortLength
                if len(orderGroup) != 0:
                    ordersGrouped.append(zip(orderGroup, carInfo, customerInfo, storeInfo))
                    if i <= 10:
                        counter.append(len(orderGroup))
                        setNames.append(lengthOfGrouping + ' ' + str(i))
                        i = i + 1
                    orderGroup = []
                    carInfo = []
                    customerInfo = []
                    storeInfo = []
            orderGroup.append(order)
            carInfo.append(Cars.objects.get(id=order.carid_id))
            customerInfo.append(Customers.objects.get(id=order.customerid_id))
            storeInfo.append(Stores.objects.get(id=order.returnstore_id))

        graphType = "None"
        if inputVeriObj.checkFormGET('Graph', 'string'):
            graphType = request.GET['Graph']
            if graphType != 'Column' and graphType != 'Pie' and graphType != 'None':
                graphType = "None"
                messages.add_message(request, messages.INFO, 'Your inputted Graph Type was not one of the options and defaulted to No Graph')


        # zippedResults = zip(ordersGrouped, carInfo, customerInfo, storeInfo)
        counterAndNames = zip(counter, setNames)
        return (ordersGrouped, counterAndNames, graphType, lengthOfGrouping, startDateFormattedForReturn, storeIDformatted)
