from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm

class ProfileForm(forms.ModelForm):

    birthday = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        input_formats=['%Y-%m-%d'],
        required=True
    )

    class Meta:
        model = Profile
        fields = ['photo','birthday']


class ProfileFormUpdate(forms.ModelForm):
    

    class Meta: 
        model = Profile
        fields = ['photo']

class CustomCreateUser(UserCreationForm):

    class Meta:
        model = User 
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']



class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'password' in self.fields:
            del self.fields['password']


class PasswordForm(PasswordChangeForm):
    pass


        

