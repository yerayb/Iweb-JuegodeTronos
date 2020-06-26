# Generated by Django 2.2.6 on 2019-11-14 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameOfThrones', '0010_auto_20191114_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('imagen', models.URLField(max_length=225, verbose_name='imagen')),
                ('lema', models.TextField()),
                ('asentamiento', models.CharField(max_length=40)),
                ('num_personajes', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Personaje',
        ),
    ]