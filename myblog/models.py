from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=3000)
    def __str__(self):
        return self.title
    
class Description(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=3000)
    def __str__(self):
        return self.title
    

