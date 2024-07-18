from django.test import TestCase
from .models import Category, Post


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Тестовая категория", slug="test-category"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Тестовая категория")
        self.assertEqual(self.category.slug, "test-category")

    def test_str_method(self):
        self.assertEqual(str(self.category), "Тестовая категория")


class PostModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Тестовая категория", slug="test-category"
        )
        self.post = Post.objects.create(
            title="Тестовый пост",
            summary="Краткое описание",
            content="<p>Основной текст поста.</p>",
            slug="test-post",
            main_image="images/test_image.jpg",
        )
        self.post.categories.add(self.category)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Тестовый пост")
        self.assertEqual(self.post.summary, "Краткое описание")
        self.assertEqual(self.post.content, "<p>Основной текст поста.</p>")
        self.assertIn(self.category, self.post.categories.all())

    def test_str_method(self):
        self.assertEqual(str(self.post), "Тестовый пост")

    def test_post_publish_date(self):
        self.assertIsNotNone(self.post.publication_date)
