from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    user_password = forms.CharField(max_length=20)

