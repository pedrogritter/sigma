from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta

from userprofiles.models import Profile
#Model imports

from examemanage.models import *

# Create your views here.
@login_required
def get_exams(request):
    user = request.user
    if user.is_student():
        query_exams =  ExameAluno.objects.filter(alunoID = user.profile)
        examesAluno = Exame.objects.filter(id = query_exams.values('exameID'))
        return render(request, 'examemanage/exams_page.html',{'exam_list': examesAluno})
    elif user.is_teacher():
        return render(request, 'examemanage/exams_page.html',{'exam_list': examesAluno})
