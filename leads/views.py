from django.shortcuts import render
from base.models import LeadForm
from icecream import ic 


def leads_list(request):
    leads = LeadForm.objects.all()
    return render(request, 'leads/leads_list.html', {'leads':leads})