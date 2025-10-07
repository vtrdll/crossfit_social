from django import forms 
from Social.models import Comment, Post, PostImage, PostVideo, StoryVideo, StoryImage
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

    
'''

class StoryImageForm(forms.ModelForm):
    class Meta:
        model = StoryImage
        fields = ['story_image']

    def validate_photos(self, files):
        errors = []
        for photo in files:
            ext = os.path.splitext(photo.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png','.webp']:
                errors.append(f"{photo.name}: extensão '{ext}' não é aceita.")
            if photo.size > 5 * 1024 * 1024:
                errors.append(f"{photo.name}: arquivo muito grande (limite 5MB).")
        return errors
    
class StoryVideoForm(forms.ModelForm):
    class Meta:
        model = StoryVideo
        fields = ['story_video']

    def validate_videos(self, files):
        errors = []
        for file in files:
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in  ['.mp4']:
                errors.append(f"{file.name}: extensão '{ext}' não é aceita. Apenas vídeos .mp4 são permitidos.")
            if file.size > 20 * 1024 * 1024:
                errors.append(f"{file.name}: arquivo muito grande (máximo 20MB).")
        return errors'''


class StoryMediaForm(forms.Form):
    

    media = forms.FileField(label="Selecione suas mídias",widget=MultipleFileInput(attrs={'multiple': True}),)
    def clean_media(self):
        files = self.files.getlist("media")
        errors = []

        if not files:
            raise forms.ValidationError("Envie pelo menos uma imagem ou vídeo.")

        for f in files:
            ext = os.path.splitext(f.name)[1].lower()

            if ext in [".jpg", ".jpeg", ".png", ".webp"]:
                if f.size > 5 * 1024 * 1024:
                    errors.append(f"{f.name}: imagem muito grande (limite 5MB).")

            elif ext == ".mp4":
                if f.size > 20 * 1024 * 1024:
                    errors.append(f"{f.name}: vídeo muito grande (limite 20MB).")

            else:
                errors.append(f"{f.name}: tipo de arquivo não suportado.")

        if errors:
            raise forms.ValidationError(errors)

        return files
    


class MultipleFileInput1(forms.ClearableFileInput):
    allow_multiple_selected = True


# Campo customizado para múltiplos arquivos
class MultipleFileField1(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput1())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        """Aceita múltiplos arquivos e valida cada um"""
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(f, initial) for f in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


# Seu form final
class StoryMediaForm(forms.Form):
    media = MultipleFileField1(
        label="Selecione suas mídias",
        required=True,
    )

    def clean_media(self):
        files = self.cleaned_data.get("media")
        errors = []

        if not files:
            raise forms.ValidationError("Envie pelo menos uma imagem ou vídeo.")

        for f in files:
            ext = os.path.splitext(f.name)[1].lower()

            if ext in [".jpg", ".jpeg", ".png", ".webp"]:
                if f.size > 5 * 1024 * 1024:
                    errors.append(f"{f.name}: imagem muito grande (limite 5MB).")

            elif ext == ".mp4":
                if f.size > 20 * 1024 * 1024:
                    errors.append(f"{f.name}: vídeo muito grande (limite 20MB).")

            else:
                errors.append(f"{f.name}: tipo de arquivo não suportado.")

        if errors:
            raise forms.ValidationError(errors)

        return files