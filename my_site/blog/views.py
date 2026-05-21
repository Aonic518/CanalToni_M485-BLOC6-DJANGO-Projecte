"""Vistes principals de l'aplicació blog."""

from django.shortcuts import render
from .models import Post, Author, Tag


def index(request):
    """
    Mostra la pàgina principal del blog.

    Aquesta vista recupera les tres publicacions més recents
    ordenades per data descendent i les envia a la plantilla
    principal del projecte.

    Args:
        request (HttpRequest):
            Objecte HTTP enviat pel client.

    Returns:
        HttpResponse:
            Renderització de la plantilla 'blog/index.html'
            amb les publicacions més recents.
    """

    latest_posts = Post.objects.all().order_by('-date')[:3]

    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    """
    Mostra totes les publicacions del blog.

    Aquesta vista obté totes les publicacions registrades
    a la base de dades i les ordena per data descendent.

    Args:
        request (HttpRequest):
            Petició HTTP del client.

    Returns:
        HttpResponse:
            Renderització de la plantilla 'blog/posts.html'
            amb totes les publicacions.
    """

    all_posts = Post.objects.all().order_by('-date')

    return render(request, 'blog/posts.html', {
        'posts': all_posts
    })


def post_detail(request, slug):
    """
    Mostra el detall d'una publicació concreta.

    La vista cerca una publicació mitjançant el seu slug
    únic i mostra tota la informació associada.

    Args:
        request (HttpRequest):
            Petició HTTP enviada pel client.

        slug (str):
            Identificador únic de la publicació.

    Returns:
        HttpResponse:
            Renderització de la plantilla
            'blog/post_detail.html' amb la informació
            de la publicació seleccionada.
    """

    identified_post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', {
        'post': identified_post
    })


def authors(request):
    """
    Mostra la llista completa d'autors.

    Aquesta vista recupera tots els autors registrats
    a la base de dades i els envia a la plantilla.

    Args:
        request (HttpRequest):
            Petició HTTP del client.

    Returns:
        HttpResponse:
            Renderització de la plantilla
            'blog/authors.html' amb tots els autors.
    """

    all_authors = Author.objects.all()

    return render(request, 'blog/authors.html', {
        'authors': all_authors
    })


def author_detail(request, author_id):
    """
    Mostra la informació detallada d'un autor.

    La vista recupera un autor específic utilitzant
    el seu identificador únic.

    Args:
        request (HttpRequest):
            Petició HTTP del client.

        author_id (int):
            Identificador de l'autor.

    Returns:
        HttpResponse:
            Renderització de la plantilla
            'blog/author_detail.html' amb la informació
            detallada de l'autor.
    """

    author = Author.objects.get(id=author_id)

    return render(request, 'blog/author_detail.html', {
        'author': author
    })


def tags(request):
    """
    Mostra totes les etiquetes disponibles.

    Aquesta vista obté totes les etiquetes
    registrades a la base de dades.

    Args:
        request (HttpRequest):
            Petició HTTP del client.

    Returns:
        HttpResponse:
            Renderització de la plantilla
            'blog/tags.html' amb totes les etiquetes.
    """

    all_tags = Tag.objects.all()

    return render(request, 'blog/tags.html', {
        'tags': all_tags
    })


def tag_posts(request, tag):
    """
    Mostra les publicacions associades a una etiqueta.

    La vista cerca una etiqueta específica i recupera
    totes les publicacions relacionades amb aquesta.

    Args:
        request (HttpRequest):
            Petició HTTP del client.

        tag (str):
            Nom de l'etiqueta utilitzada per filtrar
            publicacions.

    Returns:
        HttpResponse:
            Renderització de la plantilla
            'blog/tag_posts.html' amb les publicacions
            associades a l'etiqueta.
    """

    identified_tag = Tag.objects.get(caption=tag)

    posts = identified_tag.post_set.all()

    return render(request, 'blog/tag_posts.html', {
        'tag': identified_tag,
        'posts': posts
    })