from django.db import models
from django.contrib.auth.models import User
import time

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    artists=models.TextField()
    img=models.ImageField(upload_to="images/%Y/%m/%d")
    src=models.FileField(upload_to="audio/%Y/%m/%d")
    updated_on = models.DateTimeField(auto_now= True)
    lyrics = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
class New(models.Model):
    title=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='news')
    caption=models.ImageField(upload_to="news/img/%Y/%m%d")
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    class Meta:
        ordering=['-created_on']
    def __str__(self):
        return self.title

class Video(models.Model):
    title=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    src=models.FileField(upload_to="videos/%Y/%m/%d")
    thumbnail=models.ImageField(upload_to="videos/thumbnail/%Y/%m/%d")
    description=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_on']
    def _str__(self):
        return self.title