from email.policy import default
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image_url = models.URLField(max_length=1024, default='', blank=True)
    image = models.ImageField(default='', blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']