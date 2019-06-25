from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta
from userauth import *
from userprofiles.models import Profile
#Model imports

from examemanage.models import *
from ucmanage.models import *
# Create your views here.
@login_required
def get_exams(request):
    examesAluno = []
    user = request.user
    query_all = AlunoAulaUC.objects.all()
    query_aluno = AlunoAulaUC.objects.filter(aluno = user.profile)
    for each in query_aluno:
        examesAluno.append(Exame.objects.get(ucID = each.uc))
    return render(request, 'examemanage/exams_page.html',{'exam_list': examesAluno,})
    # elif user.is_teacher == True:
    #     # return render(request, 'examemanage/exams_page.html',{'exam_list': examesAluno},)
    #     return ''
