# Generated by Django 2.2.20 on 2021-05-05 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_criacao_postagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postagem',
            name='autor_postagem_ah',
        ),
        migrations.RemoveField(
            model_name='postagem',
            name='criacao_ptr',
        ),
        migrations.DeleteModel(
            name='Criacao',
        ),
        migrations.DeleteModel(
            name='Postagem',
        ),
    ]