from django import forms 
from Social.models import Comment, Post, PostImage, PostVideo, PostWod, StoryMedia
from django.forms.widgets import FileInput
from django.core.exceptions import ValidationError
import os

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['comment']


class PostWodForm(forms.ModelForm):

    class Meta():
        model = PostWod
        fields = ['text','title','warmup','skill','pined', 'title'] 

        labels = {
            'text': 'Texto',  
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
                'cols': 60,
                'placeholder': 'Digite o conteúdo aqui...',
                'class': 'form-control',
            }),
            'warmup': forms.Textarea(attrs={
                'rows': 5,
                'cols': 60,
                'placeholder': 'Digite o conteúdo aqui...',
                'class': 'form-control',
            }),

            'skill': forms.Textarea(attrs={
                'rows': 5,
                'cols': 60,
                'placeholder': 'Digite o conteúdo aqui...',
                'class': 'form-control',
            }),
        }
        labels = {
            'text': 'Texto',
        }
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
    photo = MultipleFileField(label='Imagem', required=False)

    class Meta:
        model = PostImage
        fields = ['photo']


    def clean(self):
        cleaned_data = super().clean()
        photos = cleaned_data.get('photo')

        if photos:
            errors = []
            for photo in photos:
                ext = os.path.splitext(photo.name)[1].lower()
                if ext not in ['.jpg', '.jpeg', '.png']:
                    errors.append(f"{photo.name}: extensão '{ext}' não é aceita.")
                if photo.size > 5 * 1024 * 1024:
                    errors.append(f"{photo.name}: arquivo muito grande (limite 5MB).")

            if errors:
                raise forms.ValidationError({'photo': errors})

        return cleaned_data
    
class VideoForm(forms.ModelForm):
    photo = MultipleFileField(label='Vídeo', required=False)

    class Meta:
        model = PostVideo
        fields = ['video']


    def clean_video(self):
        files = self.files.getlist('video')
        errors = []

        for file in files:
            ext = os.path.splitext(file.name)[1].lower()
            if ext != '.mp4':
                errors.append(f"{file.name}: extensão '{ext}' não é aceita. Apenas vídeos .mp4 são permitidos.")
            if file.size > 20 * 1024 * 1024:  # 20MB por exemplo
                errors.append(f"{file.name}: arquivo muito grande (máximo 20MB).")

        if errors:
            raise forms.ValidationError(errors)

        return files
    
class StoryForm(forms.ModelForm):
    

    class Meta:
        model = StoryMedia
        fields  =  [ 'photo', 'video']  