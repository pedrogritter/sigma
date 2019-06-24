from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from ucmanage import views as uc_views


# Create your views here.
@login_required
def get_profile(request):
    return render(request,'userprofiles/profile_page.html')
#
@login_required
def profile_details(request):
    return render(request,'userprofiles/profile_details.html')

#Schedule

@login_required
def profile_schedule(request):
    return redirect(views.profile_schedule)
    # return render(request, 'userprofiles/profile_schedule.html')

#Exams
@login_required
def profile_exams(request):
    return redirect(views.profile_exams)

# Results views
@login_required
def profile_results(request):
    return render(request, 'userprofiles/profile_results.html')
