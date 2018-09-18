import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class createAccount(forms.Form):
    name = forms.CharField(label='Name', max_length=255)  # Field name made lowercase.
    phone = forms.CharField(label='Phone', max_length=20)  # Field name made lowercase.
    address = forms.CharField(label='Address', max_length=255)  # Field name made lowercase.
    dob = forms.CharField(label='DOB', max_length=20)  # Field name made lowercase.
    occupation = forms.CharField(label='Occupation', max_length=255)  # Field name made lowercase.
    gender = forms.CharField(label='Gender', max_length=3)  # Field name made lowercase.
    email = forms.CharField(label='Email', max_length=255)  # Field name made lowercase.
    password = forms.CharField(label='Password', max_length=255)  # Field name made lowercase.

