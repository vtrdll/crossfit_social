from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Post(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, )
    date = models.DateTimeField(auto_now=True, auto_created=True)
    text = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to='media_post', null=True)



    def __str__(self):
        return f'{self.author.username} - {self.text}'
    
