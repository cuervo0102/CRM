from django.db import models

class LeadForm(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=150)



    def __str__(self) -> str:
        return (f'{self.last_name}-{self.first_name}')