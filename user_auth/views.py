from .utils import logger
from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm



def login_request(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('passowrd')
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                logger.info(f'You are now logged in as {username}.')
                return redirect('/')
            else: 
                logger.error('Invalid username or password')
        else: 
            logger.error('Invalid username or password')

    form = AuthenticationForm()
    return render(request, 'user_auth/login_request.html', {'form':form})


def logout_request(request):
    logout(request)
    return redirect('/')