from django.shortcuts import render
from .models import Cars, Customers, Stores, Orders, Profile
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from .functions.timeobjects import *
from .functions.CarPopularity import *
from .functions.search import *
from .functions.inputVerification import *
from django.contrib import messages
from .forms import *
from .functions.vehicleReturns import *
from django.core.mail import send_mail
from .functions.renderPdf import renderPDF
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from .functions.userVerification import *
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    storelist = Stores.objects.all()
    context = {'StoreList': storelist}
    return render(request, 'testApp/AlanaCustomerHomepageUpdated.html', context)

def detail(request, car_id):
    carInfo = Cars.objects.filter(id=car_id)
    context = {'CarInfo': carInfo}

    if not UserVerification.StaffLoggedIn(request):
        return render(request, 'testApp/showcaroriginal.html', context)
    post = Cars.objects.get(pk = car_id)
    if request.method == 'POST':
        if (request.POST.get('carname') and request.POST.get('carmodel') and request.POST.get('carseries') and request.POST.get('carseriesyear') and request.POST.get('carpricenew') and request.POST.get('carenginesize') and request.POST.get('carfuelsystem') and request.POST.get('cartankcapacity') and request.POST.get('carpower') and request.POST.get('carseatingcapacity') and request.POST.get('carstandardtransmission') and request.POST.get('carbodytype') and request.POST.get('cardrive') and request.POST.get('wheelbase')):
            f = forms.CharField()
            g = forms.IntegerField()
            post.car_makename = f.clean(request.POST.get('carname'))
            post.car_model = f.clean(request.POST.get('carmodel'))
            post.car_series = f.clean(request.POST.get('carseries'))
            post.car_seriesyear = g.clean(request.POST.get('carseriesyear'))
            post.car_pricenew = g.clean(request.POST.get('carpricenew'))
            post.car_enginesize = f.clean(request.POST.get('carenginesize'))
            post.car_fuelsystem = f.clean(request.POST.get('carfuelsystem'))
            post.car_tankcapacity = f.clean(request.POST.get('cartankcapacity'))
            post.car_power = f.clean(request.POST.get('carpower'))
            post.car_seatingcapacity = g.clean(request.POST.get('carseatingcapacity'))
            post.car_standardtransmission = f.clean(request.POST.get('carstandardtransmission'))
            post.car_bodytype = f.clean(request.POST.get('carbodytype'))
            post.car_drive = f.clean(request.POST.get('cardrive'))
            post.car_wheelbase = f.clean(request.POST.get('wheelbase'))
            post.save()
            messages.add_message(request, messages.INFO, 'Succefully updated car info')
    return render(request, 'testApp/showcaroriginalMikeUpdate.html', context)


def contactUs(request):
    querySuccesfullySubmitted = False
    failedToSubmit = False
    if request.method == 'POST':
        form = CustomerQuery(request.POST)
        if form.is_valid():
            subject = "Issue from: " + form.cleaned_data['your_name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['question']
            recipients = ['companyEmail@noreply.com']
            send_mail(subject, message, sender, recipients)
            querySuccesfullySubmitted = True
        else:
            failedToSubmit = True
    else:
        form = CustomerQuery()
    context = {'form': form, 'querySuccesfullySubmitted': querySuccesfullySubmitted, 'failedToSubmit': failedToSubmit}
    return render(request, 'testApp/MikeContactPage draft.html', context)

def accounts(request):
    if not UserVerification.LoggedIn(request):
        if request.method == "POST":
            if (request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('tel') and request.POST.get('bday') and request.POST.get('email') and request.POST.get('Password')):

                post = Customers()
                f = forms.CharField()
                post.name = (f.clean(request.POST.get('firstname')) + ' ' + f.clean(request.POST.get('lastname')))
                post.phone = f.clean( request.POST.get('tel'))
                post.dob = f.clean( request.POST.get('bday'))
                post.email = f.clean(request.POST.get('email'))
                post.save()
                customerUser = User.objects.create_user(username = f.clean(request.POST.get('email')), email = f.clean(request.POST.get('email')), password = f.clean(request.POST.get('Password')))
                customer_group = Group.objects.get(name = 'customer_group')
                customer_group.user_set.add(customerUser)
                customer = Profile(user=customerUser, customerid=post)
                customer.save()
                messages.add_message(request, messages.INFO, 'Account successfully created, Try logging in')
                return redirect("/")
            else:
                return render(request,'testApp/ShaleenCreateYourAccountPage.html')
        else:
            return render(request,'testApp/ShaleenCreateYourAccountPage.html')
    else:
        messages.add_message(request, messages.INFO, 'You MUST be logged out to access that page')
        return redirect("/")

def editUser(request):
    if not UserVerification.CustomerLoggedIn(request):
        messages.add_message(request, messages.INFO, 'You MUST be logged in to access that page')
        return redirect("/accounts/login/")
    userProfile = Profile.objects.get(user = request.user)
    post = Customers.objects.get(pk = userProfile.customerid_id)
    if request.method == 'POST':
        if (request.POST.get('firstname') and request.POST.get('Phonenumber') and request.POST.get('Homeaddress') and request.POST.get('DOB') and request.POST.get('youremail') and request.POST.get('Gender') and request.POST.get('Occupation')):
            f = forms.CharField()
            post.name = f.clean(request.POST.get('firstname'))
            post.phone = f.clean(request.POST.get('Phonenumber'))
            post.address = f.clean(request.POST.get('Homeaddress'))
            post.dob = f.clean(request.POST.get('DOB'))
            post.occupation = f.clean(request.POST.get('Occupation'))
            post.gender = f.clean(request.POST.get('Gender'))
            post.email = f.clean(request.POST.get('youremail'))
            post.save()
            messages.add_message(request, messages.INFO, 'Succefully updated your information')
        else:
            messages.add_message(request, messages.INFO, 'Failed to updated your information')
    dob = post.dob
    if dob[2] == "-":
        if int(dob[6:8]) < 20:
            dob = "20" + dob[6:8] + "-" + dob[3:5] + "-" + dob[0:2]
        else:
            dob = "19" + dob[6:8] + "-" + dob[3:5] + "-" + dob[0:2]

    context = {'customer': post, 'dob': dob}
    return render(request,'testApp/MikeUserLandingPage.html', context)

def staffPortal(request):
    if UserVerification.StaffLoggedIn(request):
        return render(request, 'testApp/AlanaStaffHomePage.html')
    else:
        messages.add_message(request, messages.INFO, 'You MUST be logged in to access that page')
        return redirect("/accounts/login/")


def returnPage(request):
    if UserVerification.StaffLoggedIn(request):
        zippedResults, counterAndNames, graphType, lengthOfGrouping, startDate, storeIDformatted = VehicleReturns.vehicleToBeReturned(request)
        storelist = Stores.objects.all()
        graphTitle = "The upcoming " + lengthOfGrouping +"s car returns"
        context = {'zippedResults': zippedResults, 'StoreList': storelist, 'counterAndNames': counterAndNames, 'graphTitle': graphTitle, 'graphType': graphType, 'startDate': startDate, 'storeIDformatted': storeIDformatted}
        if request.method == 'GET' and 'pdf' in request.GET:
            return renderPDF('testApp/pdf.html', context)
        return render(request, 'testApp/CarReturnsUpdatedShaleen.html', context)
    else:
        messages.add_message(request, messages.INFO, 'You MUST be logged in to access that page')
        return redirect("/accounts/login/")

def search(request):
    if request.method == 'GET':
        resultantCars = carSets.searchData(request)
    else:
        resultantCars = Cars.objects.all()

    storelist = Stores.objects.all()
    context = {'resultantCars': resultantCars, 'StoreList': storelist}
    return render(request, 'testApp/ShaleenSearchresults.html', context)

def logoutView(request):
    messages.add_message(request, messages.SUCCESS, 'Logged Out')
    logout(request)
    return redirect('/')

def successfulLogin(request):
    messages.add_message(request, messages.SUCCESS, 'Login successful')
    if UserVerification.StaffLoggedIn(request):
        return redirect("/staffPortal")
    else:
        return redirect("/")

def FAQView(request):
    return render(request, 'testApp/FAQpage.html')

def LocationsView(request):
    return render(request, 'testApp/AlanaLocations.html')

def carRecomView(request):
    if UserVerification.CustomerLoggedIn(request):
        resultantCars = carSets.reccomendCars(request)
        storelist = Stores.objects.all()
        # paginator = Paginator(resultantCars, 10)
        # page = 2
        # resultantCars = paginator.get_page(page)
        context = {'resultantCars': resultantCars, 'StoreList': storelist, 'PageType': True}
        return render(request, 'testApp/ShaleenSearchresults.html', context)
    else:
        messages.add_message(request, messages.INFO, 'You MUST be logged in to access that page')
        return redirect("/accounts/login/")

def CarPopularityView(request):
    if UserVerification.BoardMemberLoggedIn(request):
        counterAndNames, graphTitle, graphType = CarPopularity.CountCars(request)
        context = {'counterAndNames': counterAndNames, 'graphTitle': graphTitle, 'graphType': graphType}
        return render(request, 'testApp/CarpopularityupdatedShaleen.html', context)
    else:
        messages.add_message(request, messages.INFO, 'You MUST be logged in to access that page')
        return redirect("/accounts/login/")
