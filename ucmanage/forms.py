from django import forms
from ucmanage.models import *

class PedidoTrocaForm(forms.ModelForm):
    class Meta:
        model = PedidoTroca
        fields = ('aluno','aula')
    def __init__(self, user,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aluno'].initial = user.profile
        #self.fields['aula'] =
