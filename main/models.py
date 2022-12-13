from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(Author, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def snippet(self):
        return self.body[:50] + '...'
        
    
    