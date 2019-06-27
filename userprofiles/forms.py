from django import forms
from ucmanage.models import UnidadeCurricular
from userauth.models import User

from django import forms
from django.forms import ModelForm
from userprofiles.models import Profile


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','image','personal_id','address','family','birthdate']

class SignChairsForm(forms.Form):


    cadeiras = forms.MultipleChoiceField(choices=[(chairs.id, chairs.name) for chairs in UnidadeCurricular.objects.filter(cursoID = '13')], widget=forms.CheckboxSelectMultiple())

    def clean_cadeiras(self):
        if len(self.cleaned_data['cadeiras']) > 5:
            raise forms.ValidationError('Select no more than 5.')
        return self.cleaned_data['cadeiras']
