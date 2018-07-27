from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

class OrderFoodForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def __init__(self):


        #self.fields['food_id'] = forms.IntegerField(widget= \
            #forms.HiddenInput, initial=question.id)
        self.fields['quantity'] = forms.IntegerField()