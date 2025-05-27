from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "test@email.com",
            password = "secret",
        )

        cls.post = Post.objects.create(
            title = "A nice titel",
            body = "Nice body content",
            author = cls.user
        )
        cls.post2 = Post.objects.create(
            title = "A nice titel",
            body = "Nice body content",
            author = cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A nice titel")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
        self.assertEqual(self.post2.get_absolute_url(), "/post/2/")


