from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:car_id>/', views.detail, name='detail'),
<<<<<<< HEAD
    path('searchResults', views.results, name='something'),
    path('create_account/<int:customer_id>/', views.accounts, name='Accounts')
=======
    url(r'^search/$', views.search),
>>>>>>> a80a47f5d45ca643b4e9a45349f05e23077ef23d
]
