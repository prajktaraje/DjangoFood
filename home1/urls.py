from django.contrib import admin
from django.urls import path
from home1 import views


urlpatterns = [
    path("", views.index,name='home'),
    path("link/", views.link,name='link'),
    path("contact/", views.contact,name='contact'),
    path("moongdaal/", views.moongdaal,name='moongdaal bhaji'),
    path("dhokla/", views.dhokla,name='dhokla'),
    path("about/", views.about,name='aboutus'),
    path("garlicbread/", views.garlicbread,name='garlicbread'),
    path("pizzab/", views.pizzab,name='garlicbread'),
    path("momos/", views.momos,name='momos'),
    path("medu/", views.medu,name='medu'),
   
]