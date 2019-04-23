from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
    return render(request, 'userprofiles/profile_schedule.html')
