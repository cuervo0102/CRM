from django.test import TestCase, Client
from django.urls import reverse
from base.models import LeadForm

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')


    def test_index_POST(self):

        response = self.client.post(self.index_url, {
            'first_name': 'Test First Name',
            'last_name': 'Test Last Name',
            'email': 'test@test.com',
            'phone_number': '0000000000'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/')



    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/index.html')