from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:car_id>/', views.detail, name='detail'),
    path('searchResults', views.results, name='something'),
    path('create_account/<int:customer_id>/', views.accounts, name='Accounts')
]
