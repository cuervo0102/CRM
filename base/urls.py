from django.urls import path 
from .views import index, sending_email


urlpatterns = [
    path('', index), 
    path('emailing', sending_email, name='emailing')
]