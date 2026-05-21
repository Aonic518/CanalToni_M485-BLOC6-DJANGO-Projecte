"""Configuració principal de l'aplicació blog."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Classe de configuració principal de l'aplicació blog.

    Aquesta classe defineix la configuració bàsica
    necessària perquè Django registri correctament
    l'aplicació dins del projecte.
    """

    name = 'blog'