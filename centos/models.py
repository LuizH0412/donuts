from django.db import models

CHOICE_TIPO = (
    ('D', 'Doce'),
    ('S', 'Salgado')
)

class Cento(models.Model):
    valor = models.FloatField()
    quantidade = models.IntegerField()
    tipo = models.CharField(
        max_length=200,
        choices=CHOICE_TIPO
    )

    def __str__(self):
        return self.tipo
