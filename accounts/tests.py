from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .views import AuthRedirectView, AuthLoginview


class AuthRedirectViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.redirect_view = AuthRedirectView.as_view()

    def test_redirect_view_redirects_authenticated_user_to_dashboard(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.force_login(user)
        response = self.client.get(reverse_lazy('login'))
        self.assertRedirects(response, reverse_lazy('planner:dashboard'))

    def test_redirect_view_redirects_unauthenticated_user_to_login_page(self):
        response = self.client.get(reverse_lazy('planner:dashboard'))
        self.assertRedirects(response, '/account/login/?next=/planner/dashboard/')


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse_lazy('register')

    def test_register_view_returns_200(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_register_view_creates_new_user(self):
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass', 'password2': 'testpass'}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        User = get_user_model()
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_register_view_with_invalid_form_data(self):
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass', 'password2': 'wrongpass'}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        User = get_user_model()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='testuser')


class AuthLoginviewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse_lazy('login')
        self.dashboard_url = reverse_lazy('planner:dashboard')
        self.login_view = AuthLoginview.as_view()

    def test_login_view_returns_200(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_login_view_logs_in_user_with_valid_credentials(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, self.dashboard_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_does_not_log_in_user_with_invalid_credentials(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass')
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance