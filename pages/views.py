import json
from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'pages/landing_page.html')
