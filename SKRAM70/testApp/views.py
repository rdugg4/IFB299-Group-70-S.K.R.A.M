from django.shortcuts import render
from .models import Cars
from django.http import HttpResponse

def index(request):
    return render(request, 'testApp/index.html')

def detail(request, car_id):
    latest_question_list = Cars.objects.filter(id=car_id)
    context = {'CarInfo': latest_question_list}
    return render(request, 'testApp/carDetails.html', context)
