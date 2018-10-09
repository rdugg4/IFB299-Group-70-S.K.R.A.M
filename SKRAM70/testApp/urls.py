from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CarInfo/<int:car_id>/', views.detail, name='detail'),
    path('create_account/', views.accounts, name='Accounts'),
    url(r'^search/$', views.search),
    path('staffPortal', views.staffPortal, name='staffPortal'),
    url(r'^staffPortal/vehicleReturns/$', views.returnPage),
    url('ContactUs', views.contactUs, name='contactUS'),
    path('successfulLogin', views.successfulLogin, name='successfulLogin'),
    path('editUser/', views.editUser, name = 'Edit'),
    path('Locations', views.LocationsView, name="Locations"),
    path('FrequentlyAskedQuestions', views.FAQView, name="FAQs")
]
