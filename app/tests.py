from django.test import TestCase
from django.urls import reverse

from .models import Category, News


class NewsPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.uzb_category = Category.objects.create(name="Uzbekiston")
        cls.fan_category = Category.objects.create(name="Fan-texnika")

    def create_news(self, *, title="Sinov yangiligi", slug="sinov-yangiligi",
                    category=None, body="Sinov matni",
                    status=News.Status.Published):
        return News.objects.create(
            title=title,
            slug=slug,
            body=body,
            category=category or self.uzb_category,
            status=status,
        )

    def test_home_page_loads_without_news(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_news_list_page_uses_slug_detail_links(self):
        news = self.create_news()
        response = self.client.get(reverse("news_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("news_detail_page", args=[news.slug]))

    def test_published_news_detail_loads(self):
        news = self.create_news()
        response = self.client.get(
            reverse("news_detail_page", args=[news.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, news.title)

    def test_draft_news_is_not_public(self):
        news = self.create_news(
            title="Qoralama yangilik",
            slug="qoralama-yangilik",
            status=News.Status.DRAFT,
        )
        response = self.client.get(
            reverse("news_detail_page", args=[news.slug])
        )
        self.assertEqual(response.status_code, 404)

    def test_category_pages_load_without_articles(self):
        for url_name in ("uzb", "jahon", "maktab", "fan", "contact"):
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)

    def test_fan_page_displays_fan_news_body(self):
        news = self.create_news(
            title="Fan yangiligi",
            slug="fan-yangiligi",
            category=self.fan_category,
            body="Fan sahifasidagi maxsus sinov matni",
        )
        response = self.client.get(reverse("fan"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, news.body)
