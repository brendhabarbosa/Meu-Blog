from django.db import models

# Create your models here.
class Habilidade(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    descrição = models.TextField(blank=False, null=False)
    imagem = models.ImageField(upload_to='habilidades/', blank=False, null=False)

    def __str__(self):
        return self.nome

class Cursos(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    plataforma = models.CharField(max_length=100, blank=False, null=False)
    instituição = models.CharField(max_length=100, blank=False, null=False)
    imagem = models.ImageField(upload_to='cursos/', blank=False, null=False)

    def __str__(self):
        return self.nome
