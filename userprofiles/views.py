from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def get_profile(request):
    return render(request,'userprofiles/profile_page.html')
