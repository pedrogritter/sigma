from django import forms
from ucmanage.models import UnidadeCurricular
from userauth.models import User


class ProfileEditFrom(forms.Form):
    """

    """

    name = forms.CharField(
        max_length=50,
        widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right',
                'placeholder':'Change name'})
    )

    surname =  forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right',
                'placeholder':'Change surname'})
    )

    birthdate = forms.DateField(
                                widget=forms.SelectDateWidget(empty_label=("Year", "Month", "Day"))
                                )
    #
    # personal_id = None
    # address = None
    # family = None

    profession = forms.CharField(
            max_length=50,
            widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right',
                    'placeholder':'Change profession'})
        )

    personal_email = forms.EmailField(
            max_length=255,
            widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right',
                    'placeholder':'Change email'})
    )

    personal_website = forms.CharField(
            max_length=30,
            widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right',
                    'placeholder':'Change website'})
    )



def clean(self):
        cleaned_data = super(ProfileEditForm, self).clean()
        name = cleaned_data.get('name')
        surname = cleaned_data.get('surname')
        email = cleaned_data.get('email')
        profession = cleaned_data.get('profession')
        personal_email = cleaned_data.get('personal_email')
        personal_website = cleaned_data.get('personal_website')

        if not name and not email and not surname and not profession and not personal_email and not personal_website:
            raise forms.ValidationError('You have to change something!')


class SignChairsForm(forms.Form):


    cadeiras = forms.MultipleChoiceField(choices=[(chairs.id, chairs.name) for chairs in UnidadeCurricular.objects.filter(cursoID = '13')], widget=forms.CheckboxSelectMultiple())

    def clean_cadeiras(self):
        if len(self.cleaned_data['cadeiras']) > 5:
            raise forms.ValidationError('Select no more than 5.')
        return self.cleaned_data['cadeiras']
