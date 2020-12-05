from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homePage, name='home'),

    path('about/', views.aboutUs, name="about"), #introduction to Tattoo company
    path(''),
    path(''),
     path(''),


]
