from django.shortcuts import render
from .models import Cars
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

def search(request):
    if 'q' in request.GET:
        resultantCars = Cars.objects.filter(car_makename=request.GET['q'])
        context = {'resultantCars': resultantCars}
        return render(request, 'testApp/searchResults.html', context)
    # else:
    #     message = 'You submitted an empty form.'
    #     return HttpResponse(message)

    if 'pickupLocation' in request.GET:
        ordersWithCarsInLocation = Orders.objects.filter(returnstore=request.GET['pickupLocation'])
        resultantCars = Cars.objects.none()
        for order in ordersWithCarsInLocation:
            # return HttpResponse(int(str(order.returndate)[6:8]))
            carsHaveBeenReturned = ((int(request.GET['pickupDate'][0:4]) > int(str(order.returndate)[0:4])) or
                ((int(request.GET['pickupDate'][0:4]) == int(str(order.returndate)[0:4]))
                and (int(request.GET['pickupDate'][5:7]) > int(str(order.returndate)[4:6]))) or
                ((int(request.GET['pickupDate'][0:4]) == int(str(order.returndate)[0:4]))
                and (int(request.GET['pickupDate'][5:7]) == int(str(order.returndate)[4:6]))
                and (int(request.GET['pickupDate'][8:10]) >= int(str(order.returndate)[6:8]))))
            # carNotOrdered = ((int(request.GET['dropoffDate'][0:4]) > int(str(order.pickupdate)[0:4])) or
            #     ((int(request.GET['dropoffDate'][0:4]) == int(str(order.pickupdate)[0:4]))
            #     and (int(request.GET['dropoffDate'][5:7]) > int(str(order.pickupdate)[4:6]))) or
            #     ((int(request.GET['dropoffDate'][0:4]) == int(str(order.pickupdate)[0:4]))
            #     and (int(request.GET['dropoffDate'][5:7]) == int(str(order.pickupdate)[4:6]))
            #     and (int(request.GET['dropoffDate'][8:10]) >= int(str(order.pickupdate)[6:8]))))
            if (carsHaveBeenReturned):
                temp = Cars.objects.filter(id=order.carid_id)
                resultantCars = resultantCars | temp
        context = {'resultantCars': resultantCars}
        return render(request, 'testApp/searchResults.html', context)
