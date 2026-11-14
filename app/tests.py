from django.test import TestCase
from django.urls import reverse

from .models import Category, News


class NewsPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.uzb_category = Category.objects.create(name="Uzbekiston")

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_category_pages_load_without_articles(self):
        for url_name in ("uzb", "jahon", "maktab", "fan"):
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)

    def test_published_news_detail_loads(self):
        news = News.objects.create(
            title="Sinov yangiligi",
            slug="sinov-yangiligi",
            body="Sinov matni",
            category=self.uzb_category,
            status=News.Status.Published,
        )

        response = self.client.get(
            reverse("news_detail_page", args=[news.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_draft_news_is_not_public(self):
        news = News.objects.create(
            title="Qoralama yangilik",
            slug="qoralama-yangilik",
            body="Qoralama matni",
            category=self.uzb_category,
            status=News.Status.DRAFT,
        )

        response = self.client.get(
            reverse("news_detail_page", args=[news.slug])
        )
        self.assertEqual(response.status_code, 404)

    def test_sport_category_page_only_contains_sport_news(self):
        sport_category = Category.objects.create(name="Sport")
        sport_news = News.objects.create(
            title="Sport sinov yangiligi",
            slug="sport-sinov-yangiligi",
            body="Sport matni",
            category=sport_category,
            status=News.Status.Published,
        )
        other_news = News.objects.create(
            title="Boshqa kategoriya yangiligi",
            slug="boshqa-kategoriya-yangiligi",
            body="Boshqa matn",
            category=self.uzb_category,
            status=News.Status.Published,
        )

        response = self.client.get(reverse("maktab"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["sport_news"].values_list("id", flat=True)),
            [sport_news.id],
        )
        self.assertNotIn(
            other_news.id,
            response.context["sport_news"].values_list("id", flat=True),
        )
