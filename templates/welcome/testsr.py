from django.contrib.auth import SESSION_KEY, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import reverse_lazy

User = get_user_model()


class TestSignupView(TestCase, UserCreationForm):
    def setUp(self):
        self.url = reverse_lazy("accounts:signup")

    def test_success_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_success_post(self):
        valid_data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        response = self.client.post("accounts:signup", valid_data, follow=True)
        self.assertRedirects(
            response,
            reverse_lazy("tweets:home"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertTrue(User.objects.filter(username=valid_data["username"]).exists())
        self.assertIn(SESSION_KEY, self.client.session)


#     def test_failure_post_with_empty_form(self):

#     def test_failure_post_with_empty_username(self):

#     def test_failure_post_with_empty_email(self):

#     def test_failure_post_with_empty_password(self):

#     def test_failure_post_with_duplicated_user(self):

#     def test_failure_post_with_invalid_email(self):

#     def test_failure_post_with_too_short_password(self):

#     def test_failure_post_with_password_similar_to_username(self):

#     def test_failure_post_with_only_numbers_password(self):

#     def test_failure_post_with_mismatch_password(self):


# class TestLoginView(TestCase):
#     def test_success_get(self):

#     def test_success_post(self):

#     def test_failure_post_with_not_exists_user(self):

#     def test_failure_post_with_empty_password(self):


# class TestLogoutView(TestCase):
#     def test_success_post(self):


# class TestUserProfileView(TestCase):
#     def test_success_get(self):


# class TestUserProfileEditView(TestCase):
#     def test_success_get(self):

#     def test_success_post(self):

#     def test_failure_post_with_not_exists_user(self):

#     def test_failure_post_with_incorrect_user(self):


# class TestFollowView(TestCase):
#     def test_success_post(self):

#     def test_failure_post_with_not_exist_user(self):

#     def test_failure_post_with_self(self):


# class TestUnfollowView(TestCase):
#     def test_success_post(self):

#     def test_failure_post_with_not_exist_tweet(self):

#     def test_failure_post_with_incorrect_user(self):


# class TestFollowingListView(TestCase):
#     def test_success_get(self):


# class TestFollowerListView(TestCase):
#     def test_success_get(self):