from log import logger
from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout



def login_request(request): 
    
