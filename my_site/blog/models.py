"""Models principals de l'aplicació blog."""

from django.db import models


class Author(models.Model):
    """
    Model que representa un autor del blog.

    Attributes:
        first_name (CharField):
            Nom de l'autor.

        last_name (CharField):
            Cognom de l'autor.

        email (EmailField):
            Correu electrònic de l'autor.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        """
        Retorna el nom complet de l'autor.

        Returns:
            str:
                Nom i cognom concatenats.
        """

        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    """
    Model que representa una etiqueta del blog.

    Attributes:
        caption (CharField):
            Nom descriptiu de l'etiqueta.
    """

    caption = models.CharField(max_length=50)

    def __str__(self):
        """
        Retorna el nom de l'etiqueta.

        Returns:
            str:
                Text de l'etiqueta.
        """

        return self.caption


class Post(models.Model):
    """
    Model que representa una publicació del blog.

    Attributes:
        title (CharField):
            Títol de la publicació.

        excerpt (CharField):
            Descripció breu del contingut.

        image_name (CharField):
            Nom de la imatge associada.

        date (DateField):
            Data de publicació.

        slug (SlugField):
            Identificador únic URL-friendly.

        content (TextField):
            Contingut complet de la publicació.

        author (ForeignKey):
            Autor associat a la publicació.

        tags (ManyToManyField):
            Etiquetes associades.
    """

    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        """
        Retorna el títol de la publicació.

        Returns:
            str:
                Títol del post.
        """

        return self.title