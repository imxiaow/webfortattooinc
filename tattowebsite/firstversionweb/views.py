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
    #return HttpResponse('home')

def aboutUs(request):
    context = {}


    return render(request, "firstversionweb/aboutus.html", context)


def contactUs(request):
    context = {}

    return render(request, "firstversionweb/contactus.html", context)

def tattoDesign(request):
    context = {}

    return render(request, "firstversionweb/tattodesign.html", context)
