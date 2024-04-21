from django.core.management.base import BaseCommand
from base.models import LeadForm
from faker import Faker

class Command(BaseCommand):
    help = 'Seeds the database with fake data for LeadForm'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(100):  
            LeadForm.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone_number=fake.phone_number()
            )
        
        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
