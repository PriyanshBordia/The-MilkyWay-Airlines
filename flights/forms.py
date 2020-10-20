from django import forms

from .models import Passenger


class PassResetConfirmation(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(labe = "E-mail")

    # def is_valid():


class PassResetForm(forms.Form):
    newpass = forms.CharField()
