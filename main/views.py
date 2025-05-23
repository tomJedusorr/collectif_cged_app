from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articles.models import Article, ResearchPaper, ContactMessage

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def communique_view(request):
    return render(request, 'communique.html')

def analyse_view(request):
    return render(request, 'analyse.html')

def about_view(request):
    return render(request, 'about.html')

def charte_view(request):
    return render(request, 'charte.html')

@login_required
def dashboard(request):
    user_articles = Article.objects.all()
    user_papers = ResearchPaper.objects.all()
    user_messages = ContactMessage.objects.all()
    return render(request, 'dashboard.html', {
        'articles': user_articles,
        'papers': user_papers,
        'messages': user_messages
    })