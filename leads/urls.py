from django.urls import path 
from .views import leads_list


urlpatterns = [
    path('',leads_list , name='leads_list')
]