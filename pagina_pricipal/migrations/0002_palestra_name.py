# Generated by Django 3.1.7 on 2021-08-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_pricipal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='palestra',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome'),
        ),
    ]