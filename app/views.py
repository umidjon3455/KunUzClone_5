from django.shortcuts import render, get_object_or_404
from .models import Category, News


def news_list(request):
    news_list = News.published.all()
    return render(request, "news/news_list.html", {"news_list": news_list})


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)
    news_list = News.published.exclude(id=news.id)[:4]
    context = {
        "news": news,
        "news_list": news_list,
    }
    return render(request, "news/news_detail.html", context)


def home_page(request):
    news_list = News.published.all()
    minix_news = News.published.order_by("-publish_time")[:3]
    uzb_news = News.published.filter(category__name="Uzbekiston").order_by("-publish_time")[:4]
    jahon_news = News.published.filter(category__name="Jahon").order_by("-publish_time")[:4]
    sport_news = News.published.filter(category__name="Sport").order_by("-publish_time")[:2]

    fan_news = News.published.filter(
        category__name="Fan-texnika"
    ).order_by("-publish_time")

    fan_news1 = fan_news[0] if fan_news.count() > 0 else None
    fan_news2 = fan_news[1] if fan_news.count() > 1 else None
    fan_news3 = fan_news[2] if fan_news.count() > 2 else None
    fan_news4 = fan_news[3] if fan_news.count() > 3 else None

    context = {
        "news_list": news_list,
        "minix_news": minix_news,
        "uzb_news": uzb_news,
        "jahon_news": jahon_news,
        "sport_news": sport_news,
        "fan_news1": fan_news1,
        "fan_news2": fan_news2,
        "fan_news3": fan_news3,
        "fan_news4": fan_news4,
    }
    return render(request, "news/index.html", context)


def uzb_page(request):
    news_list = News.published.all()
    uzbek_news = News.published.filter(category__name="Uzbekiston")
    category_news = uzbek_news.order_by("-publish_time")
    context = {
        "news_list": news_list,
        "uzb_news_1": category_news[0],
        "uzb_news_2": category_news[1],
        "uzb_news_3": category_news[2],
        "uzb_news_4": category_news[3],
        "uzbek_news": uzbek_news,
    }
    return render(request, "news/uzb.html", context=context)


def jahon_page(request):
    jahon_news_list = News.published.all()
    jahon_news = News.published.filter(category__name="Jahon")
    category_news = jahon_news.order_by("-publish_time")
    context = {
        "jahon_news_1": category_news[0],
        "jahon_news_2": category_news[1],
        "jahon_news_3": category_news[2],
        "jahon_news_4": category_news[3],
        "jahon_news_list": jahon_news_list,
        "jahon_news": jahon_news,
    }
    return render(request, "news/single.html", context=context)


def sport_page(request):
    sport_news_list = News.published.all()
    sport_news = News.published.filter(category__name="Sport")
    category_news = sport_news.order_by("-publish_time")
    context = {
        "sport_news_1": category_news[0],
        "sport_news_2": category_news[1],
        "sport_news_3": category_news[2],
        "sport_news_4": category_news[3],
        "sport_news_list": sport_news_list,
        "sport_news": sport_news,
    }
    return render(request, "news/sport.html", context=context)


def fan_page(request):
    fan_news_list = News.published.all()
    fan_news = News.published.filter(category__name="Fan-texnika")
    category_news = fan_news.order_by("-publish_time")
    context = {
        "fan_news_1": category_news[0],
        "fan_news_2": category_news[1],
        "fan_news_3": category_news[2],
        "fan_news_4": category_news[3],
        "fan_news_list": fan_news_list,
        "fan_news": fan_news,
    }
    return render(request, "news/fan.html", context=context)


def contact_page(request):
    news_list = News.published.all()
    return render(request, "news/contact.html", {"news_list": news_list})
