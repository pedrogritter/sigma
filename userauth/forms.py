from django import forms
from ucmanage.models import Curso
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
from userauth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)



#user = get_user_model

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    curso = forms.ChoiceField(choices=[(curso.id, curso.name) for curso in Curso.objects.all()])

    class Meta:
        model = User
        fields =('email','full_name','student','teacher','curso')

    def clean_email(self):
        good_domains = ['edu','fc','ul','pt','fcul','alunos']

        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        email_domain = self.cleaned_data['email'].split('.')[-1] # Get email domain
        if qs.exists():
            raise forms.ValidationError("Email is taken, please choose another address")
        if email_domain not in good_domains:
            logger.error('This domain is not accepted: %s '% email_domain)
            raise forms.ValidationError("Registration using a non faculty email is not accepted. Please supply your academic account.", email_domain)
        return self.cleaned_data["email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        #Save the provided passsword in hashed format

        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user



class UserAdminCreationForm(forms.ModelForm):
    """
    A form that creates new users. It has all required field & repeated password
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('email','full_name','student','teacher','staff','admin')

    def clean_password(self):
        password1= self.cleaned_data.get("password1")
        password2= self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        #Save the provided passsword in hashed format

        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    full_name = forms.CharField(label='Full Name')
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'student','teacher','staff','admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
