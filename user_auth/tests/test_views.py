from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='test_username', password='password123@')

    def test_login_POST(self):
        data = {
            'username': 'test_username',
            'password': 'password123@'
        }

        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_auth/login_request.html')
