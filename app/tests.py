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
