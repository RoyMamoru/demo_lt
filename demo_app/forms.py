from django import forms
from .models import Customers

from django.forms.widgets import NumberInput


class RangeInput(NumberInput):
    input_type = 'range'
    input_oninput = "document.getElementById('output').value=this.value"

class InputForm(forms.Form):
    education_options = (
    (1, 'graduate_school'),
    (2, 'university'),
    (3, 'high school;'),
    (4, 'other'),
    )

    marital_options = (
    (1, 'married'),
    (2, 'single'),
    (3, 'others')
    )

    gender_options = (
    (1,'male'),
    (2,'female'),
    )

    payment_history = (
    (-1, 'pay'),
    (1, '1month_dalay'),
    (2, '2months_dlay')
    )

    last_name = forms.CharField(label='last_name', max_length=30, widget=forms.TextInput(attrs={'placeholder':'last_name'}))
    first_name = forms.CharField(label='first_name', max_length=30, widget=forms.TextInput(attrs={'placeholder':'first_name'}))
    limit_balance = forms.IntegerField(label='limit_balance', widget=RangeInput(attrs={'placeholder':'limit_balance'}), min_value=0, max_value=200000, initial=100000)
    sex = forms.ChoiceField(widget=forms.Select, choices=gender_options)
    education = forms.ChoiceField(choices=education_options)
    marriage = forms.ChoiceField(choices=marital_options)
    age = forms.IntegerField()
    pay_0 = forms.ChoiceField(choices=payment_history)
    pay_2 = forms.ChoiceField(choices=payment_history)
    pay_3 = forms.ChoiceField(choices=payment_history)
    pay_4 = forms.ChoiceField(choices=payment_history)
    pay_5 = forms.ChoiceField(choices=payment_history)
    pay_6 = forms.ChoiceField(choices=payment_history)
    bill_amt_1 = forms.IntegerField(label='bill_amt_1', widget=RangeInput(), min_value=-200000, max_value=100000, initial=0)
    pay_amt_1 = forms.IntegerField(label='pat_amt_1', widget=RangeInput(), min_value=0, max_value=10000, initial=5000)
    pay_amt_2 = forms.IntegerField(label='pat_amt_2', widget=RangeInput(), min_value=0, max_value=10000, initial=5000)
    pay_amt_3 = forms.IntegerField(label='pat_amt_3', widget=RangeInput(), min_value=0, max_value=10000, initial=5000)
    pay_amt_4 = forms.IntegerField(label='pat_amt_4', widget=RangeInput(), min_value=0, max_value=10000, initial=5000)
    pay_amt_5 = forms.IntegerField(label='pat_amt_5', widget=RangeInput(), min_value=0, max_value=10000, initial=5000)
    pay_amt_6 = forms.IntegerField(label='pat_amt_6', widget=RangeInput(), min_value=0, max_value=10000, initial=5000)

    class Meta:
        model = Customers
