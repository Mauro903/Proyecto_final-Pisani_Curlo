# Generated by Django 4.1.5 on 2023-02-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('duracion', models.CharField(max_length=10)),
                ('director', models.CharField(max_length=30)),
                ('fecha_estreno', models.DateField(null=True)),
                ('clasificación', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('duracion', models.CharField(max_length=10)),
                ('director', models.CharField(max_length=30)),
                ('fecha_estreno', models.DateField(null=True)),
                ('clasificación', models.CharField(max_length=50)),
            ],
        ),
    ]
