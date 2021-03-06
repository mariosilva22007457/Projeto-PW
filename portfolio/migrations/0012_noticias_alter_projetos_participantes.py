# Generated by Django 4.0.4 on 2022-05-23 15:36

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_pessoa_projetos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='projetos',
            name='participantes',
            field=models.URLField(verbose_name=portfolio.models.Pessoa),
        ),
    ]
