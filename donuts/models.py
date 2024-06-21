from django.db import models

CHOICE_TAMANHO = (
    ('P', 'Pequeno'),
    ('G', 'Grande')
)

CHOICE_TIPO = (
    ('S', 'Salgado'),
    ('D', 'Doce')
)

class Donut(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(
        max_length=200,
        choices=CHOICE_TAMANHO,
        blank=True,
        null=True
    )
    valor = models.FloatField()
    tipo = models.CharField(
        max_length=200,
        choices=CHOICE_TIPO
    )
    sabor = models.CharField(max_length=200)
    ingredientes = models.TextField()
    foto = models.ImageField(upload_to='donuts/', blank=True, null=True)


    def __str__(self):
        return self.nome
