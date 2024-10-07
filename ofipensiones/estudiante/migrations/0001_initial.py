# Generated by Django 3.2.6 on 2024-10-07 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('grado', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('codigo', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]
