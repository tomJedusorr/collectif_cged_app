from django.contrib import admin

# Register your models here.

from .models import Article, ResearchPaper, ContactMessage

admin.site.register(Article)
admin.site.register(ResearchPaper)
admin.site.register(ContactMessage)