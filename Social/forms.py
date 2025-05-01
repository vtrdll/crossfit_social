from django import forms 
from Social.models import Post, Comment



class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ['comment']
