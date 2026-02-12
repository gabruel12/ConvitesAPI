from django.db import models
from django.contrib.auth.models import User

class Convites(models.Model):
    titulo = models.CharField(max_length=30)
    conteudo = models.CharField(max_length=220)
    data = models.DateField(blank=True, null=True)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
