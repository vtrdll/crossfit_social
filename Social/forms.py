from django import forms 
from Social.models import Comment, Post
from django.core.exceptions import ValidationError
import os

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['comment']


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ['text', 'photo','video']
        
        
    

    def clean_photo (self):
        photo = self.cleaned_data.get('photo')
        
        if photo:
            ext = os.path.splitext(photo.name)[1].lower()
            if ext != '.png':
                raise forms.ValidationError("Formatação não aceita. ")
            if photo.size >  5 * 1024 * 1024: #5MB
                raise forms.ValidationError(f"O arquivo é muito grande. O tamanho máximo permitido é 5 MB.")
        return photo 
    

    def clean_video(self):
        video = self.cleaned_data.get('video')

        if video:
            ext = os.path.splitext(video.name)[1].lower()  
            if ext != '.mp4':
                raise forms.ValidationError("Apenas arquivos .mp4 são permitidos.")
                                            
            file_size = video.size
            max_size = 500 * 1024 * 1024 # 500MB 
            if file_size > max_size:
                raise ValidationError(f"O arquivo é muito grande. O tamanho máximo permitido é 1 GB.")
        return video
    