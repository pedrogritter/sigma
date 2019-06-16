from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta

#from userprofiles.models import Profile
#Model imports

from ucmanage.models import *


# Create your views here.
@login_required
def get_schedule(request):
    user = request.user

    slots = [time(8),time(8,30),time(9),time(9,30),time(10),time(10,30),time(11),time(11,30),time(12),time(12,30),time(13),time(13,30),time(14),time(14,30),time(15),time(15,30),time(16),time(16,30),time(17),time(17,30),time(18)]
    days = ['Seg','Ter','Qua','Qui', 'Sex']
    #VERIFICAR QUE USER É (PROF OU ALUNO)
    #FAZER QUERY RESPETIVA
    if user.student:
        query_user =  AlunoAulaUC.objects.filter(aluno = user.profile)
    elif user.teacher:
        query_user =  ProfessorAula.objects.filter(teacher = user.profile)




    return render(request, 'ucmanage/schedule_page.html',{'uc_list': query_user, 'slots': slots,'days':days,})
