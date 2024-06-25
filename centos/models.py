from django.db import models

CHOICE_TIPO = (
    ('D', 'Doce'),
    ('S', 'Salgado')
)

class Cento(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.FloatField()
    quantidade = models.IntegerField()
    tipo = models.CharField(
        max_length=200,
        choices=CHOICE_TIPO
    )
    foto = models.ImageField(upload_to='centos/', blank=True, null=True)

    def __str__(self):
        return self.nome
