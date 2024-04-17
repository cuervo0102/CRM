from django import forms
from .models import LeadForm

class Lead(forms.ModelForm):
    class Meta: 
        model = LeadForm
        fields = '__all__'