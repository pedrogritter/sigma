from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from .forms import RegisterForm
#from ..models import User

#Just for testing
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# import the logging library
import logging
from pages import views
from userprofiles import views


def signup(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f'Account created! You are logged in as: {user.email}')
                return redirect(views.get_profile)
            else:
                messages.error(request, f'Error creating account!')
                return render(request, 'userauth/signup.html', {'form': form})

        form = RegisterForm()
        return render(request, 'userauth/signup.html', {'form': form})
            #return redirect(views.landing)

def user_login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            #logging.logger.info('User Logged-in !')
            login(request, user)
            messages.success(request, f'Logged in: {user.email}')
            return redirect('landing')
        else:
            return render(request, 'userauth/login.html')


def user_logout(request):
        user = request.user
        if user is not None:
            email = request.user.email #use email instead of username to signout
            #username = request.user.username
            messages.warning(request, f'{email} has been logged out!')
            logout(request)
            return redirect('landing')


def authentication(request, slug):
        "Detects with authorization protocol is requested & redirects to its view"

        if slug == "signup":
                return signup(request)

        elif slug == "login":
                return user_login(request)

        elif slug == "logout":
                return user_logout(request)
