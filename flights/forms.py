from django import forms


class PassResetConfirmation(forms.Form):

    e-mail = forms.EmailField()

    def is_valid():


class PassResetForm(forms.Form):
