from django.contrib import admin

# Register your models here.

from .models import Article, ResearchPaper

admin.site.register(Article)
admin.site.register(ResearchPaper)