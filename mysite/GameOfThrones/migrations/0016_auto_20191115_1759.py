# Generated by Django 2.2.6 on 2019-11-15 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GameOfThrones', '0015_auto_20191115_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaje',
            name='temporadas',
        ),
        migrations.DeleteModel(
            name='Temporada',
        ),
    ]
