# Generated by Django 4.0.4 on 2022-05-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_post_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagem',
        ),
    ]
