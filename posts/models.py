from django.db import models
from django.contrib.auth.models import User
from topics.models import Topic
# Create your models here.
class Post(models.Model):
    """ Model to represent the post in a thread """
    content = models.TextField()
# gán về cái thread đã tạo 
    Topic = models.CharField(
        max_length=200,
        blank=True

    )
    counter_seed = models.CharField(max_length=200, null=True) 
    counter_flag = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    creator = models.CharField(max_length=200, blank=True)
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.content
