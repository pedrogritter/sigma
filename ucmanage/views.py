from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta
from .forms import PedidoTrocaForm

#from userprofiles.models import Profile
#Model imports

from ucmanage.models import *


# Create your views here.
@login_required
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
