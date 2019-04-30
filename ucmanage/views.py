from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from userprofiles.models import Profile
#Model imports

from ucmanage.models import *

# Create your views here.
@login_required
def get_schedule(request):
    user = request.user
    query_all = AlunoAulaUC.objects.all()
    query_user =  AlunoAulaUC.objects.filter(aluno = user.profile)

    return render(request, 'ucmanage/schedule_page.html',{'uc_list': query_user,})
