from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView

#from ..forms import StudentSignUpForm
#from ..models import User

#Just for testing
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# import the logging library
import logging
from pages import views


def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.success(request, f'Account created!')
                return redirect(views.landing)
            else:
                messages.error(request, f'Error creating account!')
                #return render(request, 'userauth/signup.html')

        form = UserCreationForm()
        return render(request, 'userauth/signup.html', {'form': form})
            #return redirect(views.landing)

def user_login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            #logging.logger.info('User Logged-in !')
            login(request, user)
            messages.success(request, f'Logged in: {user.username}')
            return redirect('landing')
        else:
            return render(request, 'userauth/login.html')


def user_logout(request):
        user = request.user
        if user is not None:
            username = request.user.username
            messages.warning(request, f'{username} has been logged out!')
            logout(request)
            return redirect('landing')


def authentication(request, slug):

        if slug == "signup":
                return signup(request)

        elif slug == "login":
                return user_login(request)

        elif slug == "logout":
                return user_logout(request)




# def signup(request):
#     # if request.method == "POST":
#     #     form = UserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         username= form.cleaned_data.get('username')
#     #         messages.success(request, f'Account created for {username}!')
#     #         return redirect('landing')
#     # form = UserCreationForm()
#     # return render(request, 'userauth/signup.html', {'form': form})
#
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             messages.success(request, f'Account created for {username}!')
#             return redirect('landing')
#     else:
#         form = UserCreationForm()
#     return render(request, 'userauth/signup.html', {'form': form})
#
#
# def login(request):
#     username = request.POST.get(['username'])
#     password = request.POST.get(['password'])
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect('landing')
#     else:
#         return render('authentication/login.html')
#
# def logout(request):
#     logout(request)
#     messages.success(request, f'{username} has been logged out!')
#     return redirect('landing')


# Create your views here.
# class student_signup(CreateView):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'registration/signup_form.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('views:sucess')
#
# class teacher_signup(CreateView):
#     model = User
#     form_class = TeacherSignUpForm
#     template_name = 'registration/signup_form.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'teacher'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('teachers:quiz_change_list')
