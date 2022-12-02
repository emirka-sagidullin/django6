from django import forms


class delivery(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    houseNum = forms.IntegerField()
    flat = forms.IntegerField()