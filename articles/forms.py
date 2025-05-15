from django import forms
from .models import Article, ResearchPaper
import datetime


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content', 'created_at']  # no need to include author here
        widgets = {
            'created_at': forms.DateTimeInput(
                attrs={
                    'type': 'date',  # This creates the calendar & time picker
                    'class': 'form-control',  # Optional Bootstrap class
                },
                format='%Y-%m-%d'  # HTML5 datetime-local format
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].input_formats = ['%Y-%m-%d']
        self.fields['created_at'].initial = datetime.date.today().strftime('%Y-%m-%d')

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['title', 'author', 'content', 'created_at']
        widgets = {
            'created_at': forms.DateTimeInput(
                attrs={
                    'type': 'date',  # This creates the calendar & time picker
                    'class': 'form-control',  # Optional Bootstrap class
                },
                format='%Y-%m-%d'  # HTML5 datetime-local format
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].input_formats = ['%Y-%m-%d']
        self.fields['created_at'].initial = datetime.date.today().strftime('%Y-%m-%d')
