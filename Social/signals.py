from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from .models import Post,Comment, PostCommentInventory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User


def post_inventory_update(sender, instance, **kwargs):
    user = instance.author
    post_count = Post.objects.filter(author=user).count()
    inventory, created = PostCommentInventory.objects.get_or_create(author=user)
    inventory.post_count = post_count
    inventory.save()



    
@receiver(post_save, sender = Post)
def post_inventory_save(sender, instance, **kwargs):
    post_inventory_update(sender, instance, **kwargs)
    print('instance', instance)

@receiver(post_delete, sender = Post)
def post_inventory_delete(sender, instance, **kwargs):
    post_inventory_update(sender, instance, **kwargs)







def comment_inventory_update(sender, instance, **kwargs):
    user = instance.author
    comment_count = Comment.objects.filter(author=user).count()


    inventory, created = PostCommentInventory.objects.get_or_create(author=user)

    inventory.comment_count = comment_count
    inventory.save()


@receiver(post_save, sender = Comment)
def comment_inventory_save(sender, instance, **kwargs):
    comment_inventory_update(sender, instance, **kwargs)
    print('instance', instance)



    
@receiver(post_delete, sender = Comment)
def comment_inventory_delete(sender, instance, **kwargs):
    post_inventory_update(sender, instance, **kwargs)
