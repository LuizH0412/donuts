# Generated by Django 5.0.6 on 2024-06-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cento',
            name='nome',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
