from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta
from userauth import *
from userprofiles.models import Profile
from django.shortcuts import get_list_or_404, get_object_or_404
#Model imports

from examemanage.models import *
from ucmanage.models import *
# Create your views here.

i = []
@login_required
def get_exams(request):
    global i
    examesAluno = []

    user = request.user
    query_all = AlunoAulaUC.objects.all()
    query_aluno = AlunoAulaUC.objects.filter(aluno = user.profile)
    for each in query_aluno:
        examesAluno.append(Exame.objects.get(ucID = each.uc))
    return render(request, 'examemanage/exams_page.html',{'exam_list': examesAluno, 'user': user, 'inscricoes': i })
    # elif user.is_teacher == True:
    #     # return render(request, 'examemanage/exams_page.html',{'exam_list': examesAluno},)
    #     return ''

def inscrever(request, id):
    global i
    user = request.user
    examesAluno = []
    exame = get_object_or_404(Exame, pk=id)
    i.append(exame)
    inscricao = ExameAluno.objects.create(alunoID = user.profile, exameID = exame, inscrito = True)
    inscricao.save()
    query_alunos = AlunoAulaUC.objects.filter(aluno = user.profile)
    for each in query_alunos:
        examesAluno.append(Exame.objects.get(ucID = each.uc))
    return render(request, 'examemanage/exams_page.html', {'inscricoes': i, 'exam_list': examesAluno, 'user': user})
