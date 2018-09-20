from django.shortcuts import render
from .models import Cars
from .models import Customers
from .models import Stores
from .models import Orders
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from .functions.timeobjects import *
from .functions.search import *
from .functions.inputVerification import *
from django.contrib import messages
<<<<<<< HEAD
from .forms import createAccount
from .functions.vehicleReturns import *
=======
from .forms import *
from .functions.vehicleReturns import *
from django.core.mail import send_mail
from .functions.renderPdf import renderPDF
>>>>>>> 3e9dcce143fdabcab248029d70ca05a33f5ac8a9

def index(request):
    storelist = Stores.objects.all()
    context = {'StoreList': storelist}
    return render(request, 'testApp/AlanaCustomerHomepage.html', context)

def detail(request, car_id):
    carInfo = Cars.objects.filter(id=car_id)
    context = {'CarInfo': carInfo}
    return render(request, 'testApp/showcaroriginal.html', context)

def contactUs(request):
    querySuccesfullySubmitted = False
    failedToSubmit = False
    if request.method == 'POST':
        form = CustomerQuery(request.POST)
        if form.is_valid():
            subject = "issue from: " + form.cleaned_data['your_name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['question']
            recipients = ['companyEmail@noreply.com']
            send_mail(subject, message, sender, recipients)
            querySuccesfullySubmitted = True
        failedToSubmit = True
    else:
        form = CustomerQuery()
    context = {'form': form, 'querySuccesfullySubmitted': querySuccesfullySubmitted, 'failedToSubmit': failedToSubmit}
    return render(request, 'testApp/MikeContactPage draft.html', context)

# def sign_up(request):
#     if request.method == 'POST':
#         form = createAccount(request.POST)
#         if form.is_valid():
#             post = Customers()
#             post.name = form.cleaned_data['Name']
#             post.phone = form.cleaned_data['Phone']
#             post.address = form.cleaned_data['Address']
#             post.dob = form.cleaned_data['DOB']
#             post.occupation = form.cleaned_data['Occupation']
#             post.gender = form.cleaned_data['Gender']
#             post.email = form.cleaned_data['Email']
#             post.password = form.cleaned_data['Password']
#             post.save()
#             return HttpResponse('it worked')
#             return HttpResponseRedirect('/CRC/')
#         else:
#             return HttpResponse('NOT WORKING')
#             form = createAccount()
#         return render(request, 'testApp/signup.html', {'form': form,})
#     else:
#         return render(request,'testApp/signup.html')

def accounts(request):
    if request.method == "POST":
        if (request.POST.get('Name') and request.POST.get('Phone') and request.POST.get('Address') and request.POST.get('DOB') and request.POST.get('Occupation') and request.POST.get('Gender') and request.POST.get('Email') and request.POST.get('Password')):

            post = Customers()
            f = forms.CharField()
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
    return render(request, 'testApp/MikeStaffHomePage.html')

def returnPage(request):
    zippedResults = vehicleToBeReturned(request)
    storelist = Stores.objects.all()
    context = {'zippedResults': zippedResults, 'StoreList': storelist, 'Period': zippedResults}
    if request.method == 'GET' and 'pdf' in request.GET:
        return renderPDF('testApp/pdf.html', context)
    return render(request, 'testApp/MikeCarReturnPage.html', context)

def search(request):
    resultantCars = searchData(request)
    storelist = Stores.objects.all()
    context = {'resultantCars': resultantCars, 'StoreList': storelist}
    return render(request, 'testApp/ShaleenSearchresults.html', context)
