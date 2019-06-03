from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from ucmanage import views as uc_views
from .forms import ProfileEditFrom
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages



# Create your views here.
@login_required
def get_profile(request):
    return render(request,'userprofiles/profile_page.html')

# All profile edit forms  in None
# Edit profile forms
# @login_required
# def profile_details(request):
#     if request.method=="POST":
#         form = ProfileEditFrom(request.POST)
#         password_form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             pass
#             # DO something
#             edit = form.save()
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = ProfileEditFrom()
#     return render(request,'userprofiles/profile_details.html',{'form': form})



# Edit profile forms
@login_required
def profile_details(request):
    if request.method=="POST":
        form = ProfileEditFrom(request.POST)
        if form.is_valid():
            pass
            # DO something
            edit = form.save()
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileEditFrom()
    return render(request,'userprofiles/profile_details.html',{'form': form})

# Password change
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_form = PasswordChangeForm(request.user)
    return render(request, 'userprofiles/password_change.html', {'password_form': password_form})



#Schedule
@login_required
def profile_schedule(request):
    return redirect(views.profile_schedule)
    # return render(request, 'userprofiles/profile_schedule.html')

#Exams
@login_required
def profile_exams(request):
    return render(request,'userprofiles/profile_exams.html')

# Results views
@login_required
def profile_results(request):
    return render(request, 'userprofiles/profile_results.html')
