# Generated by Django 4.1.7 on 2023-02-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_alter_autor_date_of_birth_alter_autor_date_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='date_of_death',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Died'),
        ),
    ]
