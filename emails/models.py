from django.db import models



class Email(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()