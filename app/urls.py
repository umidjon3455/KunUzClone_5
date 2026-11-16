from django.urls import path

from .views import (
    contact_page,
    fan_page,
    home_page,
    jahon_page,
    news_detail,
    news_list,
    sport_page,
    uzb_page,
)

urlpatterns = [
    path("", home_page, name="home"),
    path("maktab", sport_page, name="maktab"),
    path("jahon", jahon_page, name="jahon"),
    path("uzbekiston", uzb_page, name="uzb"),
    path("Fan-texnika", fan_page, name="fan"),
    path("contact", contact_page, name="contact"),
    path("news/", news_list, name="news_list"),
    path("news/<slug:slug>/", news_detail, name="news_detail_page"),
]
