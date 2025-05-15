"""
URL configuration for dad_cged_webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from articles import views as vi
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', vi.homepage, name='home'),
    path('article/<int:article_id>/like/', vi.like_article, name='like_article'),
    path('analyse/<int:analyse_id>/like/', vi.like_analyse, name='like_analyse'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('communique/', vi.public_articles, name='communique'),
    path('communique/<int:article_id>/', vi.article_detail, name='article_detail'),
    path('analyse/<int:paper_id>/', vi.analyse_detail, name='analyse_detail'),
    path('about/', views.about_view, name='about'),
    path('analyse/', vi.public_analyse, name='analyse'),
    path('charte/', views.charte_view, name='charte'),
    path('contact/', views.contact_view, name='contact'),
    path('create/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # for login/logout
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

