from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.create_article, name='create_article'),
    path('researchpaper/', views.create_paper, name='create_paper'),
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('researchpaper/<int:paper_id>/edit/', views.edit_paper, name='edit_paper'),
    path('researchpaper/<int:paper_id>/delete/', views.delete_paper, name='delete_paper'),
]