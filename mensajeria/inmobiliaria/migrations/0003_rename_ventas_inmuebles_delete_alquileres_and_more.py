# Generated by Django 4.0.6 on 2022-09-12 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0002_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ventas',
            new_name='Inmuebles',
        ),
        migrations.DeleteModel(
            name='Alquileres',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]