from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('coffee_app:index'))

def register(request):
    return

