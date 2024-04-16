from django.urls import path 
from .views import login_request, logout_request



urlpatterns = [
    path('', login_request, name='login_request'), 
    path('logout', logout_request, name='logout_request')
]