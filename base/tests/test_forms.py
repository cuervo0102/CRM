from django.test import TestCase
from base.forms import Lead

class LeadFormTestCase(TestCase):
    def test_lead_form_valid_data(self):
        form = Lead(data={
            'first_name': 'Test First Name',
            'last_name': 'Test Last Name',
            'email': 'test@test.com',
            'phone_number': '0000000000'
        })
        self.assertTrue(form.is_valid())

    def test_lead_form_invalid_data(self):
        form = Lead(data={})  # Empty data should be invalid
        self.assertFalse(form.is_valid())
