from django import forms

from django import forms
from django.forms import ModelForm
from userprofiles.models import Profile

# class ProfileEditFrom(forms.Form):
#     """
#
#     """
#
#     name = forms.CharField(
#         max_length=50,
#         widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right is-pulled-left',
#                 'placeholder':'Change name'},
#                 ),
#                 required=False)
#
#
#     surname =  forms.CharField(
#         max_length=100,
#         widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right is-pulled-left',
#                 'placeholder':'Change surname'}),
#                 required=False)
#
#
#     birthdate = forms.DateField(
#                                 widget=forms.SelectDateWidget(empty_label=("Year", "Month", "Day"))
#                                 )
#     #
#     # personal_id = None
#     # address = None
#     # family = None
#
#     profession = forms.CharField(
#             max_length=50,
#             widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right is-pulled-left',
#                     'placeholder':'Change profession'}),
#         required=False)
#
#     personal_email = forms.EmailField(
#             max_length=255,
#             widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right is-pulled-left',
#                     'placeholder':'Change email'}),
#         required=False)
#
#
#     personal_website = forms.CharField(
#             max_length=30,
#             widget = forms.TextInput(attrs={'style':'control has-icon has-icon-right is-pulled-left',
#                     'placeholder':'Change website'}),
#         required=False)
#
#
#
#         def clean(self):
#             cleaned_data = super(ProfileEditForm, self).clean()
#             name = cleaned_data.get('name')
#             surname = cleaned_data.get('surname')
#             email = cleaned_data.get('email')
#             profession = cleaned_data.get('profession')
#             personal_email = cleaned_data.get('personal_email')
#             personal_website = cleaned_data.get('personal_website')
#
#             if not name or not email or not surname or not profession or not personal_email or not personal_website:
#                 raise forms.ValidationError('You have to change something!')
#
#         def save(self,commit=True):
#             user_details = super(RegisterForm, self).save(commit=False)
#             user_details = self.clean()
#
#             if commit:
#                 user.save
#
#             return user

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','image','personal_id','address','family','birthdate']
