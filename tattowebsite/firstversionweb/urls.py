from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homePage, name='home'),

    path('about/', views.aboutUs, name="about"), #introduction to Tattoo company
    path('gallery/', views.galleryPage, name="gallery"),
    path('artists/', views.artistsPage, name="artists"), 
    path('tattodesign/', views.tattoDesign, name="tattodesign"), 
    path('tattooaftercare/', views.tattooAfterCarePage, name="tattooaftercare"),
    path('contact/', views.contactUs, name="contact"), 
    


    #tattodesign
    #contact
    #Artists

    #path(''),
    #path(''),
    #path(''),


]
