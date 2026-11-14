from django.shortcuts import get_object_or_404, render

from .models import News


def news_list(request):
    context = {
        "news_list": News.published.all(),
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, slug):
    news = get_object_or_404(News.published, slug=slug)
    context = {
        "news": news,
        "news_list": News.published.exclude(id=news.id)[:4],
    }
    return render(request, "news/news_detail.html", context)


def home_page(request):
    fan_news = list(
        News.published.filter(
            category__name="Fan-texnika"
        ).order_by("-publish_time")[:4]
    )

    context = {
        "news_list": News.published.all(),
        "minix_news": News.published.order_by("-publish_time")[:3],
        "uzb_news": News.published.filter(
            category__name="Uzbekiston"
        ).order_by("-publish_time")[:4],
        "jahon_news": News.published.filter(
            category__name="Jahon"
        ).order_by("-publish_time")[:4],
        "sport_news": News.published.filter(
            category__name="Sport"
        ).order_by("-publish_time")[:4],
        "fan_news1": fan_news[0] if len(fan_news) > 0 else None,
        "fan_news2": fan_news[1] if len(fan_news) > 1 else None,
        "fan_news3": fan_news[2] if len(fan_news) > 2 else None,
        "fan_news4": fan_news[3] if len(fan_news) > 3 else None,
    }

    return render(request, "news/index.html", context)


def category_page(request, category_name, template_name, prefix):
    category_news = News.published.filter(
        category__name=category_name
    ).order_by("-publish_time")

    featured = list(category_news[:4])

    context = {
        "news_list": News.published.all(),
        f"{prefix}_news_list": category_news,
        f"{prefix}_news": category_news,
    }

    for number in range(1, 5):
        context[f"{prefix}_news_{number}"] = (
            featured[number - 1]
            if len(featured) >= number
            else None
        )

    if prefix == "uzb":
        context["uzbek_news"] = category_news

    return render(request, template_name, context)


def uzb_page(request):
    return category_page(
        request, "Uzbekiston", "news/uzb.html", "uzb"
    )


def jahon_page(request):
    return category_page(
        request, "Jahon", "news/single.html", "jahon"
    )


def sport_page(request):
    return category_page(
        request, "Sport", "news/sport.html", "sport"
    )


def fan_page(request):
    return category_page(
        request, "Fan-texnika", "news/fan.html", "fan"
    )


def contact_page(request):
    context = {
        "news_list": News.published.all(),
    }
    return render(request, "news/contact.html", context)
