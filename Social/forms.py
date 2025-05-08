from django import forms 
from Social.models import Comment



class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['comment']
