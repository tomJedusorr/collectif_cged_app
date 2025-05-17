from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, ResearchPaperForm
from articles.models import Article, ResearchPaper, ArticleLike, AnalyseLike
from django.http import HttpResponseForbidden
from .forms import ContactMessageForm

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # link the logged-in user
            article.save()
            return redirect('dashboard')  # or wherever you want to go after submit
    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})


@login_required
def create_paper(request):
    if request.method == 'POST':
        form = ResearchPaperForm(request.POST)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.author = request.user
            paper.save()
            return redirect('dashboard')  # or a "paper list" view
    else:
        form = ResearchPaperForm()
    return render(request, 'articles/create_analyse.html', {'form': form})

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/create_article.html', {'form': form})

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        return render(request, 'confirm_delete_com.html', {'article': article})

    if request.method == 'POST':
        article.delete()
        return redirect('dashboard')

@login_required
def edit_paper(request, paper_id):
    analyse = get_object_or_404(ResearchPaper, id=paper_id)
    if request.method == 'POST':
        form = ResearchPaperForm(request.POST, instance=analyse)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ResearchPaperForm(instance=analyse)
    return render(request, 'articles/create_analyse.html', {'form': form})

@login_required
def delete_paper(request, paper_id):
    analyse = get_object_or_404(ResearchPaper, id=paper_id)
    if request.method == 'GET':
        return render(request, 'confirm_delete_anal.html', {'analyse': analyse})
    
    if request.method == 'POST':
        analyse.delete()
        return redirect('dashboard')

def public_articles(request):
    sort = request.GET.get('sort', 'newest')

    if sort == 'oldest':
        articles = Article.objects.order_by('created_at')
    else:  # default to newest
        articles = Article.objects.order_by('-created_at')

    return render(request, 'communique.html', {
        'articles': articles,
        'sort': sort
    })

def public_analyse(request):
    sort = request.GET.get('sort', 'newest')

    if sort == 'oldest':
        analyse = ResearchPaper.objects.order_by('created_at')
    else:  # default to newest
        analyse = ResearchPaper.objects.order_by('-created_at')

    return render(request, 'analyse.html', {
        'analyse': analyse,
        'sort': sort
    })

def homepage(request):
    recent_articles = Article.objects.order_by('-created_at')[:4]
    recent_analyses = ResearchPaper.objects.order_by('-created_at')[:4]
    
    return render(request, 'index.html', {
        'recent_articles': recent_articles,
        'recent_analyses': recent_analyses,
    })

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # Increment view count
    article.views += 1
    article.save(update_fields=['views'])

    return render(request, 'communique_detail.html', {'article': article})

def analyse_detail(request, paper_id):
    analyse = get_object_or_404(ResearchPaper, id=paper_id)

    # Increment view count
    analyse.views += 1
    analyse.save(update_fields=['views'])

    return render(request, 'analyse_detail.html', {'analyse': analyse})

def get_client_ip(request):
    """Get the real IP address of the user."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    ip = get_client_ip(request)

    # Check if this IP already liked this article
    if ArticleLike.objects.filter(article=article, ip_address=ip).exists():
        return HttpResponseForbidden("You already liked this article.")

    # Record the like
    ArticleLike.objects.create(article=article, ip_address=ip)
    article.likes += 1
    article.save(update_fields=['likes'])
    return redirect('communique')

def like_analyse(request, analyse_id):
    analyse = get_object_or_404(ResearchPaper, id=analyse_id)
    ip = get_client_ip(request)

    # Check if this IP already liked this article
    if AnalyseLike.objects.filter(analyse=analyse, ip_address=ip).exists():
        return HttpResponseForbidden("You already liked this article.")

    # Record the like
    AnalyseLike.objects.create(analyse=analyse, ip_address=ip)
    analyse.likes += 1
    analyse.save(update_fields=['likes'])
    return redirect('analyse')

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})
