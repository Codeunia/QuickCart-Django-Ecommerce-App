from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
     username = forms.CharField()
     password = forms.CharField(widget=forms.PasswordInput)
     class Meta:
        model = Customer
        fields = [ 'phone','email','address']

class CustomerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'address']  