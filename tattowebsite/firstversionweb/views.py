from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

import urllib
import json

from django.urls import reverse


# Create your views here.
def homePage(request):

    if request.method == 'POST':
        # get the form information
        firstname = request.POST.get('firstname') # grab the data
        lastname = request.POST.get('lastname')
        Artists = request.POST.get('Artists')
        emailaddress = request.POST.get('emailaddress')
        subjectmessage = request.POST.get('subjectmessage')

        info_context = {'firstname':firstname, 'lastname':lastname, 'Artists':Artists, 'emailaddress':emailaddress, 'subjectmessage':subjectmessage}

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            messages.success(request, 'Contact form submitted with success!')
            
            # send the form as email to company
            send_mail(
                'Contact Form Submission from ' + firstname + ' ' + lastname, #subject
                'The Contact Form Submission is the following: \n' + "Customer Name: " + firstname + ' ' + lastname + "\n" + "Artists: " + Artists + "\n" + "Customer Email Address: " + emailaddress + "\n" + "Message: \n" + subjectmessage + "\n", # message
                emailaddress, # senders email address
                ['info@wildcranetattoos.com'],#List of To EMail Address
                fail_silently=False
                )
            
            # automatically send an email to the form sender to confirm their submission.
            auto_send_mail_template = render_to_string("firstversionweb/automatic_email_companyToCustomer_temp.html", {'firstname':firstname})
            company_send_out_email = EmailMessage(
                'auto-reply: Contact Form Submission - ' + firstname, 
                auto_send_mail_template, 
                settings.EMAIL_HOST_USER,
                [emailaddress]
                )
            company_send_out_email.fail_silently=False
            company_send_out_email.send()

        else:
            messages.error(request, 'Error: Invalid reCAPTCHA. Please try again.')

        return redirect(reverse('home')+ "#contactform")

    else:
        context = {}
        return render(request, "firstversionweb/homepage.html", context)
    #return HttpResponse('home')


def aboutUs(request):
    context = {}

    return render(request, "firstversionweb/aboutus.html", context)


def galleryPage(request):
    context = {}
    
    return render(request, "firstversionweb/gallerypage.html", context)


def artistsPage(request):
    context = {}

    return render(request, "firstversionweb/artists.html", context)


def tattoDesign(request):
    context = {}

    return render(request, "firstversionweb/tattodesign.html", context)


def tattooAfterCarePage(request):
    context = {}

    return render(request, "firstversionweb/tattooaftercarepage.html", context)


def contactUs(request):
    context = {}

    return render(request, "firstversionweb/contactus.html", context)





