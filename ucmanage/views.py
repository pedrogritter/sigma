from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta
from .forms import PedidoTrocaForm
from django.db.models import Q

#from userprofiles.models import Profile
#Model imports

from ucmanage.models import *


# Create your views here.
@login_required(login_url='../auth/login/', redirect_field_name=None)
def get_schedule(request):
    user = request.user

    slots = [time(8),time(9),time(10),time(11),time(12),time(13),time(14),time(15),time(16),time(17),time(18)]
    days = ['Seg','Ter','Qua','Qui', 'Sex']
    #VERIFICAR QUE USER É (PROF OU ALUNO)
    #FAZER QUERY RESPETIVA
    if user.student:
        query_user =  AlunoAulaUC.objects.filter(aluno = user.profile)
    elif user.teacher:
        query_user =  ProfessorAula.objects.filter(teacher = user.profile)

    form = PedidoTrocaForm(user)

    return render(request, 'ucmanage/schedule_page.html',{'uc_list': query_user, 'slots': slots,'days':days, 'form': form})



def get_alunos_in_prof_uc(request):
    user = request.user

    if user.teacher:
        prof_aulas = ProfessorAula.objects.filter(prof = user.profile)

        alunos_inscritos = []
        prof_ucs = []
        for item in prof_aulas:
            prof_ucs.append(item.aula.turnoID.ucID)
            alunos_inscritos.append(AlunoAulaUC.objects.filter(aula = item.aula))

        for uc in prof_ucs:
            AlunoAulaUC.objects.filter(Q(uc = uc) | Q(aula__isnull=True))




    return render(request, 'ucmanage/list_alunos_uc.html',)
