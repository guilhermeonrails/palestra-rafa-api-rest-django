from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=30)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
