# Generated by Django 5.1.1 on 2024-11-27 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
                ('adresa', models.CharField(max_length=50)),
                ('grad', models.CharField(max_length=60)),
                ('drzava', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Izdavac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('adresa', models.CharField(max_length=50)),
                ('grad', models.CharField(max_length=60)),
                ('drzava', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Knjiga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=100)),
                ('datum_izdavanja', models.DateField()),
                ('authors', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.autor')),
            ],
        ),
    ]