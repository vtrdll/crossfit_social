from django.db import models
from account.models import User
from django.utils import timezone
from django.core.validators import  MinValueValidator
# Create your models here.


class Event(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    local  = models.CharField (max_length=50, default= 'null')
    title =  models.CharField (max_length=50, default= 'null')
    link =  models.URLField(max_length=100, blank= True, null= True )
    text = models.CharField(max_length=3000, blank=  True, null= True)
    date_initial = models.DateTimeField( default=  timezone.now())
    date_end = models.DateTimeField (default= timezone.now())
    date_create= models.DateTimeField(auto_now_add= True,  null= False, blank= False)
    price =  models.FloatField(validators=[MinValueValidator(0)], null= True, blank=True)

    def  __str__(self):
        return  f'Evento Criado por {self.author} no dia {self.date_create}'
    