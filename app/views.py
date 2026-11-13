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

    fan_items = list(fan_news[:4])
    fan_news1 = fan_items[0] if len(fan_items) > 0 else None
    fan_news2 = fan_items[1] if len(fan_items) > 1 else None
    fan_news3 = fan_items[2] if len(fan_items) > 2 else None
    fan_news4 = fan_items[3] if len(fan_items) > 3 else None

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


def _category_page(request, category_name, template_name, context_prefix):
    """Render a category page without crashing when it has fewer than four articles."""
    category_news = News.published.filter(
        category__name=category_name
    ).order_by("-publish_time")
    first_four = list(category_news[:4])

    context = {
        f"{context_prefix}_news_{index}": (
            first_four[index - 1] if len(first_four) >= index else None
        )
        for index in range(1, 5)
    }
    context.update({
        f"{context_prefix}_news_list": News.published.all(),
        f"{context_prefix}_news": category_news,
    })
    return render(request, template_name, context=context)


def uzb_page(request):
    return _category_page(request, "Uzbekiston", "news/uzb.html", "uzb")


def jahon_page(request):
    return _category_page(request, "Jahon", "news/single.html", "jahon")


def sport_page(request):
    return _category_page(request, "Sport", "news/sport.html", "sport")


def fan_page(request):
    return _category_page(request, "Fan-texnika", "news/fan.html", "fan")


def contact_page(request):
    news_list = News.published.all()
    return render(request, "news/contact.html", {"news_list": news_list})
