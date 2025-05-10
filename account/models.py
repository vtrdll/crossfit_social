from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media_profile', null=True)
    created_at_profile =  models.DateField(auto_now=True)
    birthday = models.DateField(max_length=50, default=timezone.now)
    


    def __str__(self):
        return f'Perfil de {self.user.username}'