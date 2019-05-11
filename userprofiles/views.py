from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from ucmanage import views as uc_views
from .forms import ProfileEditFrom


# Create your views here.
@login_required
def get_profile(request):
    return render(request,'userprofiles/profile_page.html')
#
@login_required
def profile_details(request):
    if request.method=="POST":
        form = ProfileEditFrom(request.POST)
        if form.is_valid():
            pass
            # DO something
    else:
        form = ProfileEditFrom()
    return render(request,'userprofiles/profile_details.html',{'form': form})

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
