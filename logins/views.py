from django.shortcuts import render

# Create your views here.
# from django.views import generic
# from django.contrib.auth import authenticate
# from django.utils.encoding import python_2_unicode_compatible
# from logins import models

from django.shortcuts import render
from django import forms
from logins import models
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())




