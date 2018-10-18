from .inputVerification import *
from ..models import Cars, Orders
from django.db.models import Count, Max, Min
from django.contrib import messages

class CarPopularity(object):
    def CountCars(request):
        inputVeriObj = inputVerification(request)

        counter = []
        carGroups = []
        setNames = []
        graphTitle = "Number of Car rentals"

        # Define Graph Type
        graphType = "Column"
        if inputVeriObj.checkFormGET('Graph', 'string'):
            graphType = request.GET['Graph']
            if graphType != 'Column' and graphType != 'Pie':
                graphType = "Column"
                messages.add_message(request, messages.INFO, 'Your inputted Graph Type was not one of the options and defaulted to Column')

        carsWithAnnotation = Cars.objects.annotate(numberOfOrders = Count('orders'))
        if inputVeriObj.checkFormGET('Catagory', 'string'):
            catagory = request.GET['Catagory']
            if catagory == 'seats':
                carGroups.append(carsWithAnnotation.filter(car_seatingcapacity__lte = 3))
                setNames.append("Less than 3")
                carGroups.append(carsWithAnnotation.filter(car_seatingcapacity = 4))
                setNames.append("4")
                carGroups.append(carsWithAnnotation.filter(car_seatingcapacity = 5))
                setNames.append("5")
                carGroups.append(carsWithAnnotation.filter(car_seatingcapacity = 6))
                setNames.append("6")
                carGroups.append(carsWithAnnotation.filter(car_seatingcapacity = 7))
                setNames.append("7")
                carGroups.append(carsWithAnnotation.filter(car_seatingcapacity__gte = 8))
                setNames.append("Greater than 8")
                graphTitle = graphTitle + ' divided into seat number groups'
            elif catagory == 'price':
                graphTitle = graphTitle + ' divided into new price groups'
                maximumPrice = Cars.objects.aggregate(max_price = Max('car_pricenew'))['max_price'] + 1
                minimumPrice = Cars.objects.aggregate(min_price = Min('car_pricenew'))['min_price']
                splitNumber = 10
                splitSize = int((maximumPrice - minimumPrice)/splitNumber) + 1
                i = 0
                while i < splitNumber:
                    carGroups.append(carsWithAnnotation.filter(car_pricenew__gte = (minimumPrice + i*splitSize), car_pricenew__lt = (minimumPrice + i*splitSize + splitSize)))
                    setNames.append("$" + str(minimumPrice + i*splitSize) + "-$" + str(minimumPrice + i*splitSize + splitSize))
                    i = i + 1
            elif catagory == 'driveType':
                graphTitle = graphTitle + ' divided into drive type groups'
                carGroups.append(carsWithAnnotation.filter(car_drive = "4WD"))
                setNames.append('4WD')
                carGroups.append(carsWithAnnotation.filter(car_drive = "RWD"))
                setNames.append('RWD')
                carGroups.append(carsWithAnnotation.filter(car_drive = "FWD"))
                setNames.append('FWD')
            elif catagory == 'makeName':
                graphTitle = graphTitle + ' divided into vehicle make groups'
                carMakes = carsWithAnnotation.order_by('car_makename').values('car_makename').distinct()
                for carMake in carMakes:
                    carGroups.append(carsWithAnnotation.filter(car_makename = carMake['car_makename']))
                    setNames.append(carMake['car_makename'])

            else:
                messages.add_message(request, messages.INFO, 'Your inputted Catagory was not one of the options and defaulted to driveType')

        if len(carGroups) == 0:
            graphTitle = graphTitle + ' divided into drive type groups'
            carGroups.append(carsWithAnnotation.filter(car_drive = "4WD"))
            setNames.append('4WD')
            carGroups.append(carsWithAnnotation.filter(car_drive = "RWD"))
            setNames.append('RWD')
            carGroups.append(carsWithAnnotation.filter(car_drive = "FWD"))
            setNames.append('FWD')

        i = 0
        for carGroup in carGroups:
            counter.append(0)
            for car in carGroup:
                counter[i] = counter[i] + car.numberOfOrders
            i = i + 1

        return (zip(counter, setNames), graphTitle, graphType)
