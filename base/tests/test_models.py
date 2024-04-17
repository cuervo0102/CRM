from django.test import TestCase
from base.models import LeadForm

class TestModel(TestCase): 
    def setUp(self): 
        self.initial_count = LeadForm.objects.count()

    def test_leadform_creation(self):
        LeadForm.objects.create(
            first_name='Test First Name',
            last_name='Test Last Name',
            email='test@test.com',
            phone_number='0000000000'
        )
        self.assertEqual(LeadForm.objects.count(), self.initial_count + 1)
