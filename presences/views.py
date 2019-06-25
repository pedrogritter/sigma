from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ucmanage.models import *
from .forms import PresencasForm
from .models import *
from ucmanage.models import *

# Create your views here.
#@is_student

#@is_teacher
@login_required
def PresencaListView(request):
    user = request.user

    query = ProfessorAula.objects.only('aulaID').filter(profID = user.profile)
    print(query)
    for instance in query:
        print(instance.profID)

    form = PresencasForm(user)
    return render(request,'presences/presences_page.html', {'form':form})

@login_required
def get_presencas(request):
    user = request.user

    presences = Presenca.objects.filter(aluno = user.profile)
    
    return render(request, 'presences/presenca_list.html', {'presences':presences})
