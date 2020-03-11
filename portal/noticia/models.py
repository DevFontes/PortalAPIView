from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=125)
    texto = models.TextField()
    autor = models.ForeignKey(
        "Autor", on_delete=models.PROTECT, related_name="noticias"
    )

    def __str__(self):
        return self.titulo
