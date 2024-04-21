from django.shortcuts import render, redirect
from .forms import Lead
from .tasks import send_welcome_email
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def index(request):
    form = Lead()
    if request.method == 'POST':
        form = Lead(request.POST)
        if form.is_valid():
            lead = form.save()
            send_welcome_email.delay(form.cleaned_data['email'])

            # Send notification to WebSocket clients
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'leads_group',  # Group name
                {
                    'type': 'lead_notification',
                    'lead_data': {
                        'first_name': form.cleaned_data['first_name'],
                        'last_name': form.cleaned_data['last_name'],
                        'email': form.cleaned_data['email'],
                        'phone_number': form.cleaned_data['phone_number'],
                    }
                }
            )

            return redirect('/')

    return render(request, 'base/index.html', {'form': form})
