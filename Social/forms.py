from django import forms 
from Social.models import Comment, Post, PostImage, PostVideo, StoryMedia
from django.forms.widgets import FileInput
from django.core.exceptions import ValidationError
import os

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['comment']


class PostForm(forms.ModelForm):
    pined = forms.BooleanField(required=False, label='Fixar treino no topo')
    
    class Meta():
        model = Post
        fields = ['text']



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['photo']

    def validate_photos(self, files):
        errors = []
        for photo in files:
            ext = os.path.splitext(photo.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png','.webp']:
                errors.append(f"{photo.name}: extensão '{ext}' não é aceita.")
            if photo.size > 5 * 1024 * 1024:
                errors.append(f"{photo.name}: arquivo muito grande (limite 5MB).")
        return errors
    
class VideoForm(forms.ModelForm):
    class Meta:
        model = PostVideo
        fields = ['video']

    def validate_videos(self, files):
        errors = []
        for file in files:
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in  ['.mp4']:
                errors.append(f"{file.name}: extensão '{ext}' não é aceita. Apenas vídeos .mp4 são permitidos.")
            if file.size > 20 * 1024 * 1024:
                errors.append(f"{file.name}: arquivo muito grande (máximo 20MB).")
        return errors

    
class StoryForm(forms.ModelForm):
    

    class Meta:
        model = StoryMedia
        fields  =  ['document']  