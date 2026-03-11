from django.shortcuts import render, get_object_or_404
from .models import Category, News


# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, "news/news_list.html", context=context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)

    news_list = News.published.exclude(id=news.id)[:4]
    
    context = {
        'news': news,
        'news_list': news_list
    }
    return render(request, "news/news_detail.html", context)

# from django.shortcuts import get_object_or_404, render
# from hitcount.views import HitCountDetailView
# from .models import News
#
#
# class NewsDetailView(HitCountDetailView):
#     model = News
#     template_name = 'news/news_detail.html'
#     context_object_name = 'news'
#     count_hit = True  # Bu har bir sahifa ko‘rilishini hisoblaydi
#
#
# # Agar class-based view ishlatmasangiz oddiy function-based view:
# def news_detail(request, news):
#     news = get_object_or_404(News, slug=news)
#     context = {'news': news,}
#     return render(request, 'news/news_detail.html', context)

# def home_page(request):
#     news_list = News.objects.filter(status=News.Status.Published)
#     minix_news = News.published.order_by('-publish_time')[:3]
#     uzb_news = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[:4]
#     jahon_news = News.published.filter(category__name="Jahon").order_by('-publish_time')[:4]
#     fan_news1 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[0]
#     fan_news2 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[1]
#     fan_news3 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[2]
#     fan_news4 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[3]
#
#
#
#
#     context = {
#         'news_list': news_list,
#         'minix_news': minix_news,
#         'uzb_news': uzb_news,
#         'jahon_news': jahon_news,
#         'fan_news1': fan_news1,
#         'fan_news2': fan_news2,
#         'fan_news3': fan_news3,
#         'fan_news4': fan_news4,
#     }
#
#     return render(request, "news/index.html", context)

def home_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    minix_news = News.published.order_by('-publish_time')[:3]
    uzb_news = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[:4]
    jahon_news = News.published.filter(category__name="Jahon").order_by('-publish_time')[:4]
    sport_news = News.published.filter(category__name="Sport").order_by('-publish_time')[:2]


    fan_news = News.published.filter(
        category__name="Fan-texnika"
    ).order_by('-publish_time')

    fan_news1 = fan_news[0] if fan_news.count() > 0 else None
    fan_news2 = fan_news[1] if fan_news.count() > 1 else None
    fan_news3 = fan_news[2] if fan_news.count() > 2 else None
    fan_news4 = fan_news[3] if fan_news.count() > 3 else None

    context = {
        'news_list': news_list,
        'minix_news': minix_news,
        'uzb_news': uzb_news,
        'jahon_news': jahon_news,
        'fan_news1': fan_news1,
        'fan_news2': fan_news2,
        'fan_news3': fan_news3,
        'fan_news4': fan_news4,
    }

    return render(request, "news/index.html", context)

#def home_page(request):
#    news_list = News.objects.filter(status=News.Status.Published),
#    minix_news = News.published.all().order_by('-publish_time')[:3],
#    uzb_news_1 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[0],
#     uzb_news_2 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[1],
#     uzb_news_3 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[2],
#     uzb_news_4 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[3],
#
#     context = {
#         'news_list': news_list,
#         'minix_news': minix_news,
#         'uzb_news_1': uzb_news_1,
#         'uzb_news_2': uzb_news_2,
#         'uzb_news_3': uzb_news_3,
#         'uzb_news_4': uzb_news_4,
#     }
#
#     return render(request, "news/index.html", context=context)


def uzb_page(request):
    news_list = News.objects.filter(status=News.Status.Published)
    uzbek_news = News.objects.filter(category__name="Uzbekiston")
    uzb_news_1 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[0]
    uzb_news_2 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[1]
    uzb_news_3 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[2]
    uzb_news_4 = News.published.filter(category__name="Uzbekiston").order_by('-publish_time')[3]

    context = {
        'news_list': news_list,
        'uzb_news_1': uzb_news_1,
        'uzb_news_2': uzb_news_2,
        'uzb_news_3': uzb_news_3,
        'uzb_news_4': uzb_news_4,
        'uzbek_news': uzbek_news,
    }

    return render(request, "news/uzb.html", context=context)

def jahon_page(request):
    jahon_news_list = News.objects.filter(status=News.Status.Published)
    jahon_news = News.objects.filter(category__name="Jahon")
    jahon_news_1 = News.published.filter(category__name="Jahon").order_by('-publish_time')[0]
    jahon_news_2 = News.published.filter(category__name="Jahon").order_by('-publish_time')[1]
    jahon_news_3 = News.published.filter(category__name="Jahon").order_by('-publish_time')[2]
    jahon_news_4 = News.published.filter(category__name="Jahon").order_by('-publish_time')[3]


    context = {
        'jahon_news_1': jahon_news_1,
        'jahon_news_2': jahon_news_2,
        'jahon_news_3': jahon_news_3,
        'jahon_news_4': jahon_news_4,
        'jahon_news_list': jahon_news_list,
        'jahon_news': jahon_news,
    }

    return render(request, "news/single.html", context=context)

def sport_page(request):
    sport_news_list = News.objects.filter(status=News.Status.Published)
    sport_news = News.objects.filter(category__name="Sport")
    sport_news_1 = News.published.filter(category__name="Sport").order_by('-publish_time')[0]
    sport_news_2 = News.published.filter(category__name="Sport").order_by('-publish_time')[1]
    sport_news_3 = News.published.filter(category__name="Sport").order_by('-publish_time')[2]
    sport_news_4 = News.published.filter(category__name="Sport").order_by('-publish_time')[3]



    context = {
        'sport_news_1': sport_news_1,
        'sport_news_2': sport_news_2,
        'sport_news_3': sport_news_3,
        'sport_news_4': sport_news_4,
        'sport_news_list': sport_news_list,
        'sport_news': sport_news,
    }

    return render(request, "news/sport.html", context=context)

def fan_page(request):
    fan_news_list = News.objects.filter(status=News.Status.Published)
    fan_news = News.objects.filter(category__name="Fan-texnika")
    fan_news_1 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[0]
    fan_news_2 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[1]
    fan_news_3 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[2]
    fan_news_4 = News.published.filter(category__name="Fan-texnika").order_by('-publish_time')[3]



    context = {
        'fan_news_1': fan_news_1,
        'fan_news_2': fan_news_2,
        'fan_news_3': fan_news_3,
        'fan_news_4': fan_news_4,
        'fan_news_list': fan_news_list,
        'fan_news': fan_news,
    }

    return render(request, "news/fan.html", context=context)

def contact_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, "news/contact.html", context=context)

from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("contact")

    return render(request, "news/contact.html")