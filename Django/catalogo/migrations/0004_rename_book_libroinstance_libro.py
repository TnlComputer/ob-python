# Generated by Django 4.1.7 on 2023-02-16 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_alter_autor_date_of_birth_alter_autor_date_of_death'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libroinstance',
            old_name='book',
            new_name='libro',
        ),
    ]