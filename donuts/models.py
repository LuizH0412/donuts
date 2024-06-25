from django.db import models

CHOICE_TIPO = (
    ('S', 'Salgado'),
    ('D', 'Doce')
)

class Donut(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=200,
        choices=CHOICE_TIPO
    )
    ingredientes = models.TextField()
    foto = models.ImageField(upload_to='donuts/', blank=True, null=True)


    def __str__(self):
        return self.nome
