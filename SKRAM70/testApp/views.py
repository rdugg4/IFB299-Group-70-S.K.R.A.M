from django.shortcuts import render
from .models import Cars
from .models import Customers
from django.http import HttpResponse

def index(request):
    return render(request, 'testApp/index.html')

def detail(request, car_id):
    carInfo = Cars.objects.filter(id=car_id)
    context = {'CarInfo': carInfo}
    return render(request, 'testApp/carDetails.html', context)

def results(request):
    resultantCars = Cars.objects.filter(car_makename="LAND ROVER")
    context = {'resultantCars': resultantCars}
    return render(request, 'testApp/searchResults.html', context)

def accounts(request, customer_id):
    customerInfo = Customers.objects.filter(id=customer_id)
    context = {'CustomerInfo': customerInfo}
    return render(request, 'testApp/signup.html', context)

