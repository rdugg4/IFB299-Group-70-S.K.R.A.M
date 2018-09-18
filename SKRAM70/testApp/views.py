from django.shortcuts import render
from .models import Cars
from .models import Customers
from .models import Stores
from .models import Orders
from django.http import HttpResponse
from django import forms
from .functions.timeobjects import *
from .functions.search import *
from .functions.inputVerification import *
from .functions.vehicleReturns import *

def index(request):
    storelist = Stores.objects.all()
    context = {'StoreList': storelist}
    return render(request, 'testApp/index.html', context)

def detail(request, car_id):
    carInfo = Cars.objects.filter(id=car_id)
    context = {'CarInfo': carInfo}
    return render(request, 'testApp/showcaroriginal.html', context)

def accounts(request):
    if request.method == "POST":
        if (request.POST.get('Name') and request.POST.get('Phone') and request.POST.get('Address') and request.POST.get('DOB') and request.POST.get('Occupation') and request.POST.get('Gender') and request.POST.get('Email') and request.POST.get('Password')):

            post = Customers()
            f = forms.CharField()
            f.clean(request.POST.get('Name'))
            post.name = f.clean(request.POST.get('Name'))
            post.phone = f.clean( request.POST.get('Phone'))
            post.address = f.clean( request.POST.get('Address'))
            post.dob = f.clean( request.POST.get('DOB'))
            post.occupation = f.clean( request.POST.get('Occupation'))
            post.gender = f.clean( request.POST.get('Gender'))
            post.email = f.clean(request.POST.get('Email'))
            post.password = f.clean(request.POST.get('Password'))
            post.save()
            return render(request, 'testApp/signup.html')
        else:
            return render(request,'testApp/signup.html')
    else:
        return render(request,'testApp/signup.html')

def staffPortal(request):
    return render(request, 'testApp/staffPortal.html')

def returnPage(request):
    zippedResults = vehicleToBeReturned(request)
    storelist = Stores.objects.all()
    context = {'zippedResults': zippedResults, 'StoreList': storelist}
    return render(request, 'testApp/returnPage.html', context)

def search(request):
    resultantCars = searchData(request)
    storelist = Stores.objects.all()
    context = {'resultantCars': resultantCars, 'StoreList': storelist}
    return render(request, 'testApp/searchResults.html', context)
