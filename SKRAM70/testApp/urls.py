from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:car_id>/', views.detail, name='detail'),
    path('create_account/', views.accounts, name='Accounts'),
    url(r'^search/$', views.search),
    path('staffPortal', views.staffPortal, name='staffPortal'),
    url(r'^staffPortal/vehicleReturns/$', views.returnPage),
    url('ContactUs', views.contactUs, name='contactUS')
]