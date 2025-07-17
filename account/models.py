from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.





class Profile (models.Model):
    BOX_CHOICES = (('CF4TIME CAMPINA ', 'CF4TIME CAMPINA'), ('CF4TIME CAMPINA', 'CF4TIME JOCKEY'))

    CATEGORY_CHOICES = (('FITNESS', 'FITNESS'), ('SCALED','SCALED'),('AMADOR', 'AMADOR'), ('RX','RX',), ('MASTER', 'MASTER'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media_profile', null=True, blank=True)
    created_at_profile =  models.DateField(auto_now=True)
    birthday = models.DateField(max_length=50, default=timezone.now)
    category = models.CharField(choices= CATEGORY_CHOICES, default= 'EXPERIMENTAL')
    box = models.CharField(choices = BOX_CHOICES, default = 'DEFAULT')

    def __str__(self):
        return f'Perfil de {self.user.username}'