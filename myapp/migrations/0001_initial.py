# Generated by Django 5.1.7 on 2025-04-08 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Nombre Parque')),
                ('description', models.TextField(verbose_name='Descripcion Parque')),
            ],
        ),
    ]
