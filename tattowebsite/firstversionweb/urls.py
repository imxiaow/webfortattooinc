from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homePage, name='home'),

    path('about/', views.aboutUs, name="about"), #introduction to Tattoo company
    path('contact/', views.contactUs, name="contact"), 
    path('tattodesign/', views.tattoDesign, name="tattodesign"), 

    #tattodesign
    #contact
    #Artists

    #path(''),
    #path(''),
    #path(''),


]
