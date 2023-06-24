from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100, blank=True)
    description=models.TextField(max_length=1000, blank=True)
    image_link=models.CharField(max_length=1000, default='', blank=True)
    video_link=models.CharField(max_length=1000, default='', blank=True)
    bg_image_link=models.CharField(max_length=1000, default='', blank=True)
    year=models.CharField(max_length=4, default='', blank=True)
    mins=models.CharField(max_length=3, default= '', blank=True)
    ratings=models.CharField(max_length=3, default='', blank=True)
    genere=models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.title
    

class Description(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=5000)
    image_link=models.CharField(max_length=1000, default='')
    def __str__(self):
        return self.title
    
