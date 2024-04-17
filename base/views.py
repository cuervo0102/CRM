from django.shortcuts import render, redirect
from .forms import Lead
from icecream import ic 
from django.http import HttpResponse
from .models import LeadForm
from .tasks import send_welcome_email




def index(request):
    form = Lead()
    if request.method == 'POST':
        form = Lead(request.POST)
        if form.is_valid():
            form.save()
            send_welcome_email.delay(form.cleaned_data['email'])
            ic(request.POST)
            return redirect('/')
            
    return render(request, 'base/index.html', {'form': form})


