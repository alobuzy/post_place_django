from django.db import models

from django.conf import settings
    
class Post(models.Model):
    title = models.CharField(max_length=32, blank=False)
    text = models.TextField(max_length=1024)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=1024)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(blank=True, null=True)