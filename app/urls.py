from django.contrib import admin
from django.urls import path, include

from . import views
from .views import news_list, news_detail, home_page, uzb_page, jahon_page, sport_page,fan_page,contact_page

urlpatterns = [
    path('', home_page, name='home'),
    path('maktab', sport_page, name='maktab'),
    path('jahon', jahon_page, name='jahon'),
    path('uzbekiston', uzb_page, name='uzb'),
    path('Fan-texnika', fan_page, name='fan'),
    path('contact', contact_page, name='contact'),
    path("news/<slug:slug>/", news_detail, name='news_detail_page'),
    path("contact/", views.contact, name="contact"),
]