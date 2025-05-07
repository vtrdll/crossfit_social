from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']



class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username']


class PasswordForm(PasswordChangeForm):
    pass


        

