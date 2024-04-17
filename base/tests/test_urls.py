from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import index


class TestURL(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)