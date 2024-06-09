from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tweet

User = get_user_model()


class TestHomeView(TestCase):
    def setUp(self):
        self.url = reverse("tweets:home")
        self.user = User.objects.create(
            username="test_user",
            password="test_password",
        )
        self.tweet = Tweet.objects.create(user=self.user, title="test_title", content="test_content")

    def test_success_get(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tweets_list"]), list(Tweet.objects.all()))
        self.assertTemplateUsed(response, "tweets/home.html")


class TestTweetCreateView(TestCase):
    def setUp(self):
        self.url = reverse("tweets:create")
        self.user = User.objects.create(
            username="testesuser",
        )
        self.user.set_password("testpassword")
        self.user.save()

    def test_success_get(self):
        self.client.force_login(self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tweets/post.html")

    def test_success_post(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, {"title": "test_title", "content": "test_content"})
        expected_url = reverse("tweets:home")
        self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.first().content, "test_content")

    def test_failure_post_with_empty_content(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, data={"title": "test_title", "content": ""})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "content", "このフィールドは必須です。")

    def test_failure_post_with_too_long_content(self):
        self.client.force_login(self.user)
        response = self.client.post(self.url, data={"title": "test_title", "content": "test_content" * 100})
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("この値は 100 文字以下でなければなりません( 1200 文字になっています)。", form.errors["content"])


class TestTweetDetailView(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user",
        )
        self.client.force_login(self.user)
        self.tweet = Tweet.objects.create(user=self.user, title="test_title", content="test_content")
        self.url = "/tweets/" + str(self.tweet.id) + "/"

    def test_success_get(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tweets"][0], self.tweet)
        self.assertTemplateUsed(response, "tweets/detail.html")


class TestTweetDeleteView(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user",
        )
        self.user2 = User.objects.create(
            username="test_user2",
        )
        self.client.force_login(self.user)
        self.tweet = Tweet.objects.create(user=self.user, title="test_title", content="test_content")
        self.tweet2 = Tweet.objects.create(user=self.user2, title="testtt_title", content="testtt_content")
        self.url = "/tweets/" + str(self.tweet.id) + "/delete/"
        self.othersurl = "/tweets/" + str(self.tweet2.id) + "/delete/"
        self.wrongurl = "/tweets/" + str("48956984-1c8b-6e38-2d6a-548a6b1c50f0") + "/delete/"

    def test_success_post(self):
        response = self.client.post(self.url)
        expected_url = reverse("tweets:home")
        self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)
        self.assertFalse(Tweet.objects.filter(id=self.tweet.id).exists())

    def test_failure_post_with_not_exist_tweet(self):
        response = self.client.post(self.wrongurl)
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Tweet.objects.filter(id=self.tweet.id).exists())

    def test_failure_post_with_incorrect_user(self):
        response = self.client.post(self.othersurl)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Tweet.objects.filter(id=self.tweet2.id).exists())


# class TestLikeView(TestCase):
#     def test_success_post(self):

#     def test_failure_post_with_not_exist_tweet(self):

#     def test_failure_post_with_liked_tweet(self):


# class TestUnLikeView(TestCase):

#     def test_success_post(self):

#     def test_failure_post_with_not_exist_tweet(self):

#     def test_failure_post_with_unliked_tweet(self):
