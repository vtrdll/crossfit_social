from django.db import models


from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.





class Profile (models.Model):
    BOX_CHOICES = (('CF4TIME CAMPINA ', 'CF4TIME CAMPINA'), ('CF4TIME CAMPINA', 'CF4TIME JOCKEY'))
    GENRE_CHOICES =(('MASCULINO', 'MASCULINO'),  ('FEMININO','FEMININO'), ('NÃO-ESPECIFICAR','NÃO-ESPECIFICAR'))
    CATEGORY_CHOICES = (('FITNESS', 'FITNESS'), ('SCALED','SCALED'),('AMADOR', 'AMADOR'), ('RX','RX',), ('MASTER', 'MASTER'))
    genre = models.CharField(choices=GENRE_CHOICES, default = 'NÃO-ESPECIFICAR')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media_profile', null=True, blank=True)
    created_at_profile =  models.DateField(auto_now=True)
    birthday = models.DateField(max_length=50, default=timezone.now)
    weight = models.DecimalField(max_digits= 5, decimal_places = 2, validators=[MaxValueValidator (300), MinValueValidator(0)], default=0)
    height = models.DecimalField(max_digits= 5, decimal_places = 2,  default=0)
    category = models.CharField(choices= CATEGORY_CHOICES, default= 'EXPERIMENTAL')
    box = models.CharField(choices = BOX_CHOICES, default = 'DEFAULT')
    is_coach = models.BooleanField(default=False,)
    def __str__(self):
        return f'Perfil de {self.user.username}'