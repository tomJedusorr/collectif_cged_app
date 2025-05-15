from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    author = models.CharField(max_length=100, default="Collectif CGED")
    created_at = models.DateField()
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class ResearchPaper(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    author = models.CharField(max_length=100, default="Collectif CGED")
    created_at = models.DateField()
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class ArticleLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes_by_ip')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('article', 'ip_address')  # only one like per article per IP

class AnalyseLike(models.Model):
    analyse = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE, related_name='likes_by_ip')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('analyse', 'ip_address')  # only one like per article per IP
