# Generated by Django 4.2.9 on 2024-01-31 11:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("alumnos", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="alumno",
            name="genero",
        ),
    ]