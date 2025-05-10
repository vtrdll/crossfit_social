from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Post(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, )
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    text = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to='media_post', null=True, blank= True)



    def __str__(self):
        return f'{self.author.username} - {self.text}'
    


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    post  = models.ForeignKey(Post, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.author.username} - {self.comment}'
    

class PostCommentInventory(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_inventory')
    post_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author} - {self.post_count} - {self.comment_count}'