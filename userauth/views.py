from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

#from ..forms import StudentSignUpForm
#from ..models import User

#Jsut for testing
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    return render(request, 'userauth/signup.html', {'form': form})


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
