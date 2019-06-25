from django import forms
from .models import Presenca
from userprofiles.models import Profile
from ucmanage.models import *

class PresencasForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ('aula','date','aluno')

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aula'].queryset = ProfessorAula.objects.filter(profID = user.profile).only('aulaID')
        self.fields['aluno'].queryset = AlunoAulaUC.objects.none()
