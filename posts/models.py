from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
    author=models.ForeignKey(User,related_name='post_author',on_delete=models.SET_NULL,null=True,blank=True)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=500)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='photo_image')
    tags = TaggableManager()
    category=models.ForeignKey('Category',related_name='post_category',on_delete=models.SET_NULL,null=True,blank=True)
    draft=models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user=models.CharField(max_length=100)
    post=models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE)
    publish_date=models.DateTimeField(default=timezone.now)
    content=models.TextField(max_length=500)

    def __str__(self):
        return str(self.post)

