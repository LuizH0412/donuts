# Generated by Django 5.0.6 on 2024-06-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('tipo', models.CharField(choices=[('D', 'Doce'), ('S', 'Salgado')], max_length=200)),
            ],
        ),
    ]
