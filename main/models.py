from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


class Comment(BaseModel):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return f"{self.post.title} - {self.author.username}"

    
        
