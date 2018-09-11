import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ConfirmDate(forms.Form):
    date_confirmation = forms.DateField(help_text="Enter a date in the future")

    def clean_renewal_date(self):
        data = self.cleaned_data['date_confirmation']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Remember to always return the cleaned data.
        return data
