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

#Exams
@login_required
def profile_exams(request):
    return render(request,'userprofiles/profile_exams.html')

# Results views
@login_required
def profile_results(request):
    return render(request, 'userprofiles/profile_results.html')
