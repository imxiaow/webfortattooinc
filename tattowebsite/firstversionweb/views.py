from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages



# Create your views here.
def homePage(request):
    context = {}


    return render(request, "firstversionweb/homepage.html", context)


def aboutUs(request):
    context = {}


    return render(request, "firstversionweb/aboutus.html", context)

