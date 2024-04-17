from django.shortcuts import render
from .forms import Lead
from icecream import ic 
from django.http import HttpResponse
from .models import LeadForm
from .tasks import send_email_task




def index(request):
    form = Lead()
    if request.method == 'POST':
        form = Lead(request.POST)
        if form.is_valid():
            form.save()

            ic(request.POST)
    return render(request, 'base/index.html', {'form': form})


def sending_email(request):
    subject = 'Welcome to CRM world'
    message = 'Hi Siham, thank you for registering on CRM.'
    recipient_list = ['blackbutlersiham2001@gmail.com']
    send_email_task.delay(subject, message, recipient_list)

    return HttpResponse('Email sent asynchronously')