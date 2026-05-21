"""Configuració de rutes de l'aplicació blog."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='posts-detail-page'),

    path('authors', views.authors, name='authors-page'),
    path('authors/<int:author_id>', views.author_detail, name='author-detail-page'),

    path('tags', views.tags, name='tags-page'),
    path('tags/<str:tag>', views.tag_posts, name='tag-posts-page'),
]