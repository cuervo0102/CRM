from django.urls import path 
from .views import login_request



urlpatterns = [
    path('', login_request, name='login_request')
]