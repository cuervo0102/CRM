from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user_auth.views import login_request, logout_request


class TestUrls(SimpleTestCase):



    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_request)


    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_request)